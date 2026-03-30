from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Artista, Evento, Producto, Release, Podcast
from .serializers import (
    ArtistaSerializer,
    EventoSerializer,
    ProductoSerializer,
    ReleaseSerializer,
    PodcastSerializer,
)

# Create your views here.

class EsGestorOAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated and
            (request.user.es_gestor or request.user.es_admin)
        )


class ArtistaListCreateAPI(generics.ListCreateAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ArtistaDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artista.objects.all()
    serializer_class = ArtistaSerializer
    permission_classes = [EsGestorOAdmin]


class EventoListCreateAPI(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class EventoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EsGestorOAdmin]


class ProductoListCreateAPI(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsGestorOAdmin]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ProductoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [EsGestorOAdmin]