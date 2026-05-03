"""
URL configuration for synthgrooveBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from synthgrooveApp.views import (
    ArtistaListCreateAPI, ArtistaDetailAPI,
    EventoListCreateAPI, EventoDetailAPI,
    ProductoListCreateAPI, ProductoDetailAPI,RegisterAPIView, LoginAPIView, LogoutAPIView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("api/artistas/", ArtistaListCreateAPI.as_view(), name="api_artistas"),
    path("api/artistas/<int:pk>/", ArtistaDetailAPI.as_view(), name="api_artista_detail"),

    path("api/eventos/", EventoListCreateAPI.as_view(), name="api_eventos"),
    path("api/eventos/<int:pk>/", EventoDetailAPI.as_view(), name="api_evento_detail"),

    path("api/productos/", ProductoListCreateAPI.as_view(), name="api_productos"),
    path("api/productos/<int:pk>/", ProductoDetailAPI.as_view(), name="api_producto_detail"),

    path("api/auth/register/", RegisterAPIView.as_view(), name="api_register"),
    path("api/auth/login/", LoginAPIView.as_view(), name="api_login"),
    path("api/auth/logout/", LogoutAPIView.as_view(), name="api_logout"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="api_token_refresh"),
]
