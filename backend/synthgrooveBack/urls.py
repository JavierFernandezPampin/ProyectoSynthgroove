from django.contrib import admin
from django.urls import path, re_path
from synthgrooveApp.views import (
    ArtistaListCreateAPI,
    EventoListCreateAPI, EventoDetailAPI,
    ProductoListCreateAPI,
    ReleaseListCreateAPI,
    PodcastListCreateAPI,
    RegisterAPIView, LoginAPIView, LogoutAPIView,
    MeAPIView, PedidosAPIView, ChangePasswordAPIView,
    PagoStripeAPIView,
    stripe_webhook,
    UsuariosAdminAPIView,
    ProductoDetailAPI,
)
from rest_framework_simplejwt.views import TokenRefreshView
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/artistas/", ArtistaListCreateAPI.as_view(), name="api_artistas"),

    path("api/eventos/", EventoListCreateAPI.as_view(), name="api_eventos"),
    path("api/eventos/<int:pk>/", EventoDetailAPI.as_view(), name="api_evento_detail"),

    path("api/productos/", ProductoListCreateAPI.as_view(), name="api_productos"),
    path("api/productos/<int:pk>/", ProductoDetailAPI.as_view(), name="api_producto_detail"),
    path("api/pago/stripe/", PagoStripeAPIView.as_view(), name="api_pago_stripe"),
    path("api/webhook/", stripe_webhook, name="api_stripe_webhook"),

    path("api/releases/", ReleaseListCreateAPI.as_view(), name="api_releases"),

    path("api/podcasts/", PodcastListCreateAPI.as_view(), name="api_podcasts"),

    path("api/auth/register/", RegisterAPIView.as_view(), name="api_register"),
    path("api/auth/login/", LoginAPIView.as_view(), name="api_login"),
    path("api/auth/logout/", LogoutAPIView.as_view(), name="api_logout"),
    path("api/auth/me/", MeAPIView.as_view(), name="api_me"),
    path("api/auth/change-password/", ChangePasswordAPIView.as_view(), name="api_change_password"),
    path("api/auth/refresh/", TokenRefreshView.as_view(), name="api_token_refresh"),

    path("api/pedidos/", PedidosAPIView.as_view(), name="api_pedidos"),

    path("api/admin/usuarios/", UsuariosAdminAPIView.as_view(), name="api_admin_usuarios"),
    path("api/admin/usuarios/<int:pk>/", UsuariosAdminAPIView.as_view(), name="api_admin_usuario_delete"),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
