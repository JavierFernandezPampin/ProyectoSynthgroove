
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP
import stripe
from .models import Artista, Evento, Producto, Release, Podcast, Usuario, Pago, Pedido
from .serializers import (
    ArtistaSerializer,
    EventoSerializer,
    ProductoSerializer,
    ReleaseSerializer,
    PodcastSerializer,
    UsuarioSerializer,
    PedidoSerializer
)
# Create your views here.

DESCUENTO_AUTENTICADO = Decimal("0.80")
CENTIMOS = Decimal("100")
CENTIMO = Decimal("0.01")

#controla quien puede acceder a una vista
class EsGestorOAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated and
            request.user.rol in ['gestor', 'admin']
        )

#artista
class ArtistaListCreateAPI(generics.ListCreateAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)


#release
class ReleaseListCreateAPI(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [EsGestorOAdmin] 

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)


#podctast
class PodcastListCreateAPI(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)


#eventos
class EventoListCreateAPI(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)


class EventoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EsGestorOAdmin]


#productos
class ProductoListCreateAPI(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)


#login , register ,logout 

class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        mail = request.data.get("mail")
        usuario = request.data.get("usuario")
        password = request.data.get("password")

        if not mail or not usuario or not password:
            return Response({"error": "Todos los campos son obligatorios."}, status=400)

        if Usuario.objects.filter(mail=mail).exists():
            return Response({"error": "El email ya está en uso."}, status=400)

        if Usuario.objects.filter(usuario=usuario).exists():
            return Response({"error": "El nombre de usuario ya está en uso."}, status=400)

        user = Usuario.objects.create_user(mail=mail, usuario=usuario, password=password)
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "usuario": user.usuario,
            "rol": user.rol,
        }, status=201)


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        mail = request.data.get("mail")
        password = request.data.get("password")

        user = Usuario.objects.authenticate(mail, password)
        if not user:
            return Response({"error": "Credenciales incorrectas."}, status=401)

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "usuario": user.usuario,
            "rol": user.rol,
        })


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Sesión cerrada correctamente."})
        except Exception:
            return Response({"error": "Token inválido."}, status=400)


class MeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)


class DebugPagosAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Endpoint para debug: ver pagos del usuario"""
        pagos = Pago.objects.filter(usuario=request.user)
        data = {
            'pagos_totales': pagos.count(),
            'pagos': [
                {
                    'id': p.id,
                    'producto': p.producto.nombre if p.producto else None,
                    'evento': p.evento.nombre if p.evento else None,
                    'cantidad': p.cantidad,
                    'monto': str(p.monto),
                    'pagado': p.pagado,
                    'fecha': p.fecha.isoformat() if p.fecha else None,
                    'stripe_session_id': p.stripe_session_id
                }
                for p in pagos.order_by('-fecha')
            ]
        }
        return Response(data)


class PruebaWebhookAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """
        Endpoint para probar la creación de Pedidos manualmente.
        Simula lo que hace el webhook.
        """
        pago_id = request.data.get('pago_id')
        
        if not pago_id:
            return Response({'error': 'pago_id requerido'}, status=400)
        
        try:
            pago = Pago.objects.get(id=pago_id, usuario=request.user)
        except Pago.DoesNotExist:
            return Response({'error': 'Pago no encontrado'}, status=404)
        
        logger.warning(f"🧪 TEST WEBHOOK - Pago: {pago}")
        
        # Asegurarse que está pagado
        pago.pagado = True
        pago.save()
        
        if not pago.producto:
            return Response({'error': 'Pago sin producto - es probablemente un evento'}, status=400)
        
        if not pago.usuario:
            return Response({'error': 'Pago sin usuario'}, status=400)
        
        # Verificar que no exista ya
        pedido_existe = Pedido.objects.filter(
            usuario=pago.usuario,
            producto=pago.producto,
            cantidad=pago.cantidad
        ).exists()
        
        if pedido_existe:
            return Response({'message': 'Pedido ya existe'}, status=400)
        
        try:
            precio_unitario = Decimal(str(pago.monto)) / Decimal(str(pago.cantidad)) if pago.cantidad > 0 else Decimal(str(pago.monto))
            
            pedido = Pedido.objects.create(
                usuario=pago.usuario,
                producto=pago.producto,
                cantidad=pago.cantidad,
                precio_unitario=precio_unitario
            )
            logger.warning(f"🎉 PEDIDO CREADO EN TEST: ID={pedido.id}")
            
            return Response({
                'success': True,
                'pedido_id': pedido.id,
                'usuario': pago.usuario.usuario,
                'producto': pago.producto.nombre,
                'cantidad': pago.cantidad,
                'precio_unitario': str(precio_unitario)
            })
        except Exception as e:
            logger.error(f"❌ Error en test: {str(e)}", exc_info=True)
            return Response({'error': str(e)}, status=500)

class SincronizarPedidosAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Sincroniza los pagos confirmados con la tabla de Pedidos"""
        # Solo usuarios autenticados pueden sincronizar sus propios pedidos
        pagos = Pago.objects.filter(
            usuario=request.user,
            pagado=True,
            producto__isnull=False
        )
        
        creados = 0
        existentes = 0
        errores = []
        
        for pago in pagos:
            # Verificar si ya existe un Pedido
            pedido_existe = Pedido.objects.filter(
                usuario=pago.usuario,
                producto=pago.producto,
                cantidad=pago.cantidad
            ).exists()
            
            if pedido_existe:
                existentes += 1
                continue
            
            try:
                if pago.cantidad > 0:
                    precio_unitario = Decimal(pago.monto) / Decimal(pago.cantidad)
                else:
                    precio_unitario = pago.monto
                
                Pedido.objects.create(
                    usuario=pago.usuario,
                    producto=pago.producto,
                    cantidad=pago.cantidad,
                    precio_unitario=precio_unitario
                )
                creados += 1
            except Exception as e:
                errores.append(str(e))
        
        return Response({
            'status': 'success',
            'pagos_encontrados': pagos.count(),
            'pedidos_creados': creados,
            'pedidos_existentes': existentes,
            'errores': errores
        })
    
    def get(self, request):
        """Ver estado de pagos del usuario"""
        pagos = Pago.objects.filter(usuario=request.user)
        pedidos = Pedido.objects.filter(usuario=request.user)
        
        pagos_data = [
            {
                'id': p.id,
                'producto': p.producto.nombre if p.producto else None,
                'evento': p.evento.nombre if p.evento else None,
                'cantidad': p.cantidad,
                'monto': str(p.monto),
                'pagado': p.pagado,
                'fecha': p.fecha.isoformat() if p.fecha else None,
            }
            for p in pagos.order_by('-fecha')
        ]
        
        return Response({
            'pagos_totales': pagos.count(),
            'pagos_confirmados': pagos.filter(pagado=True).count(),
            'pedidos_totales': pedidos.count(),
            'pagos': pagos_data
        })


class PedidosAPIView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user).order_by('-fecha')


class ChangePasswordAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            return Response({"error": "Todos los campos son obligatorios."}, status=400)

        user = request.user
        if not user.check_password(old_password):
            return Response({"error": "La contraseña actual es incorrecta."}, status=400)

        if len(new_password) < 6:
            return Response({"error": "La contraseña debe tener al menos 6 caracteres."}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({"message": "Contraseña cambiada exitosamente."})
        


#pago stripe
class PagoStripeAPIView(APIView):
    def get_permissions(self):
        tipo = self.request.data.get('tipo')
        # Require authentication for products (to save order)
        # Allow anonymous for events
        if tipo == 'producto':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def post(self, request):
        self.check_permissions(request)
        
        tipo = request.data.get('tipo') 
        obj_id = request.data.get('id')
        cantidad = int(request.data.get('cantidad', 1))

        if tipo == 'producto':
            obj = Producto.objects.filter(id=obj_id).first()
        elif tipo == 'evento':
            obj = Evento.objects.filter(id=obj_id).first()
        else:
            return Response({'error': 'Tipo inválido'}, status=400)

        if not obj:
            return Response({'error': 'No encontrado'}, status=404)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        es_autenticado = request.user.is_authenticated
        precio_base = obj.precio
        precio_unitario = (
            (precio_base * DESCUENTO_AUTENTICADO).quantize(CENTIMO, rounding=ROUND_HALF_UP)
            if es_autenticado
            else precio_base
        )
        monto_total = precio_unitario * cantidad
        unit_amount = int(
            (precio_unitario * CENTIMOS).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
        )

        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {'name': getattr(obj, 'nombre', str(obj))},
                        'unit_amount': unit_amount,
                    },
                    'quantity': cantidad,
                }],
                mode='payment',
                success_url=f'{settings.FRONTEND_URL}/',
                cancel_url=f'{settings.FRONTEND_URL}/compra-cancelada',
            )

            Pago.objects.create(
                usuario=request.user if es_autenticado else None,
                producto=obj if tipo == 'producto' else None,
                evento=obj if tipo == 'evento' else None,
                cantidad=cantidad,
                monto=monto_total,
                stripe_session_id=session.id,
                pagado=False
            )

            return Response({'checkout_url': session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=500)


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    
    logger.warning(f"🔔 WEBHOOK RECIBIDO - Sig: {sig_header is not None}")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError) as e:
        logger.error(f"❌ Error en verificación de firma: {str(e)}")
        return HttpResponse(status=400)

    logger.warning(f"✓ Evento válido: {event['type']}")

    if event['type'] == 'checkout.session.completed':
        session_id = event['data']['object']['id']
        logger.warning(f"💳 Session completada: {session_id}")
        
        pago = Pago.objects.filter(stripe_session_id=session_id).first()
        logger.warning(f"📦 Pago encontrado: {pago}")
        
        if pago:
            # Marcar como pagado
            pago.pagado = True
            pago.save()
            logger.warning(f"✅ Pago {pago.id} marcado como pagado")
            
            # Crear Pedido si es un producto
            if pago.producto:
                if not pago.usuario:
                    logger.warning(f"⚠️  Pago sin usuario asociado - No se crea Pedido")
                    return HttpResponse(status=200)
                
                # Verificar que no exista ya
                pedido_existe = Pedido.objects.filter(
                    usuario=pago.usuario,
                    producto=pago.producto,
                    cantidad=pago.cantidad
                ).exists()
                
                if pedido_existe:
                    logger.warning(f"⚠️  Pedido ya existe - No se duplica")
                    return HttpResponse(status=200)
                
                try:
                    # Crear el Pedido
                    precio_unitario = Decimal(str(pago.monto)) / Decimal(str(pago.cantidad)) if pago.cantidad > 0 else Decimal(str(pago.monto))
                    
                    pedido = Pedido.objects.create(
                        usuario=pago.usuario,
                        producto=pago.producto,
                        cantidad=pago.cantidad,
                        precio_unitario=precio_unitario
                    )
                    logger.warning(f"🎉 PEDIDO CREADO: ID={pedido.id}, Usuario={pago.usuario.usuario}, Producto={pago.producto.nombre}, Cantidad={pago.cantidad}")
                    return HttpResponse(status=200)
                    
                except Exception as e:
                    logger.error(f"❌ Error creando Pedido: {str(e)}", exc_info=True)
                    return HttpResponse(status=500)
            else:
                logger.warning(f"⚠️  Pago sin producto - Probablemente es un evento")
                return HttpResponse(status=200)
        else:
            logger.warning(f"❌ Pago no encontrado para session {session_id}")
            return HttpResponse(status=200)
    
    logger.warning(f"⏭️  Evento ignorado: {event['type']}")
    return HttpResponse(status=200)
