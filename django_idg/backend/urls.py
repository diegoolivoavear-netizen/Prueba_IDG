# tu_app/urls.py
from django.urls import path
from backend.views import UsuarioListCreateAPIView, UsuarioDetailAPIView
from frontend.views import home
urlpatterns = [
    path('', home, name='home'),
    path('usuarios/', UsuarioListCreateAPIView.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetailAPIView.as_view(), name='usuario-detail'),
]