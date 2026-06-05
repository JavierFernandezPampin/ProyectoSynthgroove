from rest_framework import serializers
from .models import Artista, Release, Podcast, Evento, Producto, Usuario, Pedido
import cloudinary


def _cloudinary_https(imagen):
    if not imagen:
        return None
    url = cloudinary.utils.cloudinary_url(str(imagen))[0]
    return url.replace("http://", "https://")


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

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['imagen'] = _cloudinary_https(instance.imagen)
        return ret


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['imagen'] = _cloudinary_https(instance.imagen)
        return ret


class ArtistaSerializer(serializers.ModelSerializer):
    podcasts = PodcastSerializer(many=True, read_only=True)
    releases = ReleaseSerializer(many=True, read_only=True)
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        return _cloudinary_https(obj.imagen)

    class Meta:
        model = Artista
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'usuario', 'nombre', 'apellido', 'mail', 'rol']


class PedidoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    producto_imagen = serializers.SerializerMethodField()

    def get_producto_imagen(self, obj):
        return _cloudinary_https(obj.producto.imagen if obj.producto else None)

    class Meta:
        model = Pedido
        fields = ['id', 'producto', 'producto_nombre', 'producto_imagen', 'cantidad', 'precio_unitario', 'fecha']
