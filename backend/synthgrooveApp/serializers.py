from rest_framework import serializers
from .models import Artista, Release, Podcast, Evento, Producto, Usuario, Pedido
import os

#el serializer sirve para convertir los datos a json y poder leerlos en la web y viceversa
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        usuario = Usuario(**validated_data)
        if password:
            usuario.set_password(password)
        else:
            usuario.set_unusable_password()
        usuario.save()
        return usuario

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance



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
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None

    class Meta:
        model = Producto
        fields = "__all__"

class ArtistaSerializer(serializers.ModelSerializer):
    podcasts = PodcastSerializer(many=True, read_only=True)
    releases = ReleaseSerializer(many=True, read_only=True)
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        if obj.imagen:
            return obj.imagen.url
        return None

    class Meta:
        model = Artista
        fields = "__all__"
class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
