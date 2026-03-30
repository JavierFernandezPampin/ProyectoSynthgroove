from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    ROLE= [
        ("gestor", "Gestor"),
        ("suscriptor", "Suscriptor"),
        ("admin", "Administrador"),
    ]

    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLE, default="suscriptor")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    @property #convierte un metodo en atributo 
    def es_suscriptor(self):
        return self.is_authenticated and self.rol == "suscriptor"

    @property
    def es_gestor(self):
        return self.is_authenticated and self.rol == "gestor"

    @property
    def es_admin(self):
        return self.is_authenticated and self.rol == "admin"

    
    def __str__(self):
        return f"{self.email} - {self.rol}"


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="artistas/", blank=True, null=True)

    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="artistas")

    def __str__(self):
        return self.nombre


class Release(models.Model):
    titulo = models.CharField(max_length=150)
    url = models.URLField()
    imagen = models.ImageField(upload_to="releases/", blank=True, null=True)
    fecha_release = models.DateField()
    
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE,related_name="releases")
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="releases")

    def __str__(self):
        return self.titulo


class Podcast(models.Model):
    titulo = models.CharField(max_length=150)
    url = models.URLField()
    imagen = models.ImageField(upload_to="podcasts/", blank=True, null=True)
    fecha_release = models.DateField()

    artista = models.ForeignKey(Artista,on_delete=models.CASCADE,related_name="podcasts")
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="podcasts"    )

    def __str__(self):
        return self.titulo


class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    localizacion = models.CharField(max_length=200)
    fecha_evento = models.DateField()
    imagen = models.ImageField(upload_to="eventos/", blank=True, null=True)

    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="eventos")

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    CATEGORIA= [
        ("camiseta", "Camiseta"),
        ("sudadera", "Sudadera"),
        ("accesorio", "Accesorio"),
        ("otro", "Outro"),
    ]

    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to="productos/", blank=True, null=True)
    categoria = models.CharField(max_length=50, choices=CATEGORIA, default="otro")

    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="productos")

    def __str__(self):
        return f"{self.nombre} - {self.precio}€"