from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.generic.edit import CreateView, FormView

from rest_framework import generics, permissions

from .models import Artista, Evento, Producto, Release, Podcast, Usuario
from .serializers import (
    ArtistaSerializer,
    EventoSerializer,
    ProductoSerializer,
    ReleaseSerializer,
    PodcastSerializer
)

from .forms import RegistroForm, LoginForm

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

class ArtistaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [EsGestorOAdmin]


#release
class ReleaseListCreateAPI(generics.ListCreateAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)

class ReleaseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [EsGestorOAdmin]


#podctast
class PodcastListCreateAPI(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(creado_por=self.request.user)

class PodcastDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = [EsGestorOAdmin]


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

        try:
            user = Usuario.objects.get(mail=mail)
        except Usuario.DoesNotExist:
            return Response({"error": "Credenciales incorrectas."}, status=401)

        if not user.check_password(password):
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