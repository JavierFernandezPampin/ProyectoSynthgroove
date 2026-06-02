from rest_framework import serializers
from .models import Artista, Release, Podcast, Evento, Producto
import cloudinary

#el serializer sirve para convertir los datos a json y poder leerlos en la web y viceversa
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
        if obj.imagen:
            url = cloudinary.utils.cloudinary_url(str(obj.imagen))[0]
            return url.replace("http://", "https://")
        return None

    class Meta:
        model = Evento
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    imagen = serializers.SerializerMethodField()

    def get_imagen(self, obj):
        if obj.imagen:
            url = cloudinary.utils.cloudinary_url(str(obj.imagen))[0]
            return url.replace("http://", "https://")   
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
            url = cloudinary.utils.cloudinary_url(str(obj.imagen))[0]
            return url.replace("http://", "https://")
        return None

    class Meta:
        model = Artista
        fields = "__all__"
