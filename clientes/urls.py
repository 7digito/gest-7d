from django.urls import path
from . import views
from .views import lista_clientes

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('', lista_clientes, name='lista_clientes'),

]
