from rest_framework import serializers
from .models import Artista, Release, Podcast, Evento, Producto


class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = "__all__"


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"