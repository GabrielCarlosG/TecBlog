from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_postagens, name='listar_postagens'),
]
