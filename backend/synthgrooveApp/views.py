from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from django.conf import settings
from decimal import Decimal, ROUND_HALF_UP
import logging
import stripe

from .models import Artista, Evento, Producto, Release, Podcast, Usuario, Pago, Pedido
from .serializers import (
    ArtistaSerializer,
    EventoSerializer,
    ProductoSerializer,
    ReleaseSerializer,
    PodcastSerializer,
    UsuarioSerializer,
    PedidoSerializer,
)

logger = logging.getLogger(__name__)

DESCUENTO_AUTENTICADO = Decimal("0.80")
CENTIMOS = Decimal("100")
CENTIMO = Decimal("0.01")


class EsGestorOAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.rol in ['gestor', 'admin']


class ArtistaListCreateAPI(generics.ListCreateAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [EsGestorOAdmin]


class ReleaseListCreateAPI(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [EsGestorOAdmin]


class PodcastListCreateAPI(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [EsGestorOAdmin]


class EventoListCreateAPI(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EsGestorOAdmin]


class EventoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EsGestorOAdmin]


class ProductoListCreateAPI(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsGestorOAdmin]


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
            token = RefreshToken(request.data.get("refresh"))
            token.blacklist()
            return Response({"message": "Sesión cerrada correctamente."})
        except Exception:
            return Response({"error": "Token inválido."}, status=400)


class MeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response(UsuarioSerializer(request.user).data)


class ChangePasswordAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            return Response({"error": "Todos los campos son obligatorios."}, status=400)
        if not request.user.check_password(old_password):
            return Response({"error": "La contraseña actual es incorrecta."}, status=400)
        if len(new_password) < 6:
            return Response({"error": "La contraseña debe tener al menos 6 caracteres."}, status=400)

        request.user.set_password(new_password)
        request.user.save()
        return Response({"message": "Contraseña cambiada exitosamente."})


class PedidosAPIView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pedido.objects.filter(usuario=self.request.user).order_by('-fecha')


class EsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == 'admin'


class PedidosAdminAPIView(generics.ListAPIView):
    serializer_class = PedidoSerializer
    permission_classes = [EsAdmin]

    def get_queryset(self):
        return Pedido.objects.select_related('usuario', 'producto').order_by('-fecha')


class UsuariosAdminAPIView(APIView):
    permission_classes = [EsAdmin]

    def get(self, request):
        usuarios = Usuario.objects.exclude(rol='admin').order_by('usuario')
        data = UsuarioSerializer(usuarios, many=True).data
        return Response(data)

    def patch(self, request, pk):
        try:
            usuario = Usuario.objects.exclude(rol='admin').get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=404)
        nuevo_rol = request.data.get('rol')
        if nuevo_rol not in ['suscriptor', 'gestor']:
            return Response({'error': 'Rol inválido'}, status=400)
        usuario.rol = nuevo_rol
        usuario.save()
        return Response(UsuarioSerializer(usuario).data)

    def delete(self, request, pk):
        try:
            usuario = Usuario.objects.exclude(rol='admin').get(pk=pk)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=404)
        usuario.delete()
        return Response(status=204)


class ProductoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsGestorOAdmin]


class PagoStripeAPIView(APIView):
    def get_permissions(self):
        if self.request.data.get('tipo') == 'producto':
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
        precio_unitario = (
            (obj.precio * DESCUENTO_AUTENTICADO).quantize(CENTIMO, rounding=ROUND_HALF_UP)
            if es_autenticado else obj.precio
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
                success_url=f'{settings.FRONTEND_URL}/#/compra-exitosa',
                cancel_url=f'{settings.FRONTEND_URL}/#/compra-cancelada',
            )

            Pago.objects.create(
                usuario=request.user if es_autenticado else None,
                producto=obj if tipo == 'producto' else None,
                evento=obj if tipo == 'evento' else None,
                cantidad=cantidad,
                monto=monto_total,
                stripe_session_id=session.id,
                pagado=False,
            )

            return Response({'checkout_url': session.url})
        except Exception as e:
            return Response({'error': str(e)}, status=500)


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError) as e:
        logger.error(f"Webhook firma inválida: {e}")
        return HttpResponse(status=400)

    if event['type'] != 'checkout.session.completed':
        return HttpResponse(status=200)

    session_id = event['data']['object']['id']
    pago = Pago.objects.filter(stripe_session_id=session_id).first()

    if not pago:
        logger.warning(f"Pago no encontrado para session {session_id}")
        return HttpResponse(status=200)

    if pago.pagado:
        return HttpResponse(status=200)

    pago.pagado = True
    pago.save()

    if not pago.producto or not pago.usuario:
        return HttpResponse(status=200)

    try:
        precio_unitario = (
            Decimal(str(pago.monto)) / Decimal(str(pago.cantidad))
            if pago.cantidad > 0 else Decimal(str(pago.monto))
        )
        pedido = Pedido.objects.create(
            usuario=pago.usuario,
            producto=pago.producto,
            cantidad=pago.cantidad,
            precio_unitario=precio_unitario,
        )
        logger.info(f"Pedido {pedido.id} creado: {pago.usuario.usuario} - {pago.producto.nombre}")
    except Exception as e:
        logger.error(f"Error creando Pedido: {e}", exc_info=True)
        return HttpResponse(status=500)

    return HttpResponse(status=200)
