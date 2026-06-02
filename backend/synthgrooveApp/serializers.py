from rest_framework import serializers
from .models import Artista, Release, Podcast, Evento, Producto
import cloudinary
from django.core.cache import cache

#el serializer sirve para convertir los datos a json y poder leerlos en la web y viceversa

# Función auxiliar para obtener URLs de Cloudinary con caché
def get_cloudinary_url(imagen):
    """Obtiene URL de Cloudinary con caché para evitar llamadas repetidas"""
    if not imagen:
        return None
    
    imagen_str = str(imagen)
    cache_key = f"cloudinary_url_{imagen_str}"
    
    # Intentar obtener del caché
    cached_url = cache.get(cache_key)
    if cached_url:
        return cached_url
    
    # Si no está en caché, calcular y guardar
    try:
        url = cloudinary.utils.cloudinary_url(imagen_str)[0]
        url = url.replace("http://", "https://")
        cache.set(cache_key, url, timeout=86400)  # Caché por 24 horas
        return url
    except:
        return None


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"


class EventoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        return get_cloudinary_url(obj.imagen)

    class Meta:
        model = Evento
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        return get_cloudinary_url(obj.imagen)

    class Meta:
        model = Producto
        fields = "__all__"

class ArtistaSerializerBasico(serializers.ModelSerializer):
    """Serializer básico de Artista SIN releases/podcasts (más rápido para listados)"""
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        return get_cloudinary_url(obj.imagen)

    class Meta:
        model = Artista
        fields = ["id", "nombre", "descripcion", "imagen", "instagram", "soundcloud", "usuario"]


class ArtistaSerializer(serializers.ModelSerializer):
    """Serializer completo de Artista CON releases y podcasts"""
    podcasts = PodcastSerializer(many=True, read_only=True)
    releases = ReleaseSerializer(many=True, read_only=True)
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        return get_cloudinary_url(obj.imagen)

    class Meta:
        model = Artista
        fields = "__all__"
