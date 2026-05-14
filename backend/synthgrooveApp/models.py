from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Manager para Usuario personalizado
class UsuarioManager(BaseUserManager):
    def create_user(self, mail, usuario, password=None, **extra_fields):
        if not mail:
            raise ValueError('El email es requerido')
        email = self.normalize_email(mail)
        user = self.model(mail=email, usuario=usuario, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, usuario, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('rol', 'admin')
        return self.create_user(mail, usuario, password, **extra_fields)


# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ("gestor", "Gestor"),
        ("suscriptor", "Suscriptor"),
        ("admin", "Administrador"),
    ]

    usuario = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    mail = models.EmailField(unique=True)
    rol = models.CharField(max_length=20, choices=ROLE_CHOICES, default="suscriptor")
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['usuario']

    class Meta:
        db_table = 'synthgrooveApp_usuario'

    def __str__(self):
        return f"{self.usuario} - {self.rol}"


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="artistas/", blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    soundcloud = models.URLField(blank=True, null=True)
    
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="artistas")

    def __str__(self):
        return self.nombre


class Release(models.Model):
    titulo = models.CharField(max_length=150)
    url = models.URLField()
    imagen = models.ImageField(upload_to="releases/", blank=True, null=True)
    fecha_release = models.DateField(null=True, blank=True)
    
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE,related_name="releases")
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="releases")

    def __str__(self):
        return self.titulo


class Podcast(models.Model):
    title = models.CharField(max_length=150)
    url = models.URLField()
    imagen = models.ImageField(upload_to="podcasts/", blank=True, null=True)
    fecha_release = models.DateField(null=True, blank=True)

    artista = models.ForeignKey(Artista,on_delete=models.CASCADE,related_name="podcasts")
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,blank=True,related_name="podcasts")

    def __str__(self):
        return self.title


class Evento(models.Model):
    nombre = models.CharField(max_length=150)
    localizacion = models.CharField(max_length=200)
    fecha_release = models.DateField(null=True, blank=True)
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


class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="pedidos")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="pedidos")
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.usuario.usuario}"
