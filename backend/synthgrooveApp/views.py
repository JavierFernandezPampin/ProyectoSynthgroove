
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from django.conf import settings
from django.core.mail import send_mail
import stripe
from .models import Artista, Evento, Producto, Release, Podcast, Usuario, Pago
from .serializers import (
    ArtistaSerializer,
    EventoSerializer,
    ProductoSerializer,
    ReleaseSerializer,
    PodcastSerializer
)
# Create your views here.

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

class ProductoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsGestorOAdmin]


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
        


#pago stripefrom decimal import Decimal

class PagoStripeAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            print("=== INICIO PAGO ===")
            print("user:", request.user)
            print("autenticado:", request.user.is_authenticated)
            print("stripe key:", settings.STRIPE_SECRET_KEY[:10] if settings.STRIPE_SECRET_KEY else "NONE")

            tipo = request.data.get('tipo') 
            obj_id = request.data.get('id')
            cantidad = int(request.data.get('cantidad', 1))
            print("tipo:", tipo, "id:", obj_id, "cantidad:", cantidad)

            if tipo == 'producto':
                obj = Producto.objects.filter(id=obj_id).first()
            elif tipo == 'evento':
                obj = Evento.objects.filter(id=obj_id).first()
            else:
                return Response({'error': 'Tipo inválido'}, status=400)

            print("obj:", obj)
            if not obj:
                return Response({'error': 'No encontrado'}, status=404)

            stripe.api_key = settings.STRIPE_SECRET_KEY
            es_autenticado = request.user.is_authenticated
            precio_unitario = obj.precio * Decimal('0.8') if es_autenticado else obj.precio
            print("precio_unitario:", precio_unitario)

            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {'name': getattr(obj, 'nombre', str(obj))},
                        'unit_amount': round(float(precio_unitario) * 100),
                    },
                    'quantity': cantidad,
                }],
                mode='payment',
                success_url=f'{settings.FRONTEND_URL}/compra-exitosa?session_id={{CHECKOUT_SESSION_ID}}',
                cancel_url=f'{settings.FRONTEND_URL}/compra-cancelada',
            )
            print("session creada:", session.id)

            Pago.objects.create(
                usuario=request.user if es_autenticado else None,
                producto=obj if tipo == 'producto' else None,
                evento=obj if tipo == 'evento' else None,
                cantidad=cantidad,
                monto=precio_unitario * cantidad,
                stripe_session_id=session.id,
                pagado=False
            )

            return Response({'checkout_url': session.url})

        except Exception as e:
            import traceback
            print("=== ERROR ===")
            traceback.print_exc()
            return Response({'error': str(e)}, status=500)