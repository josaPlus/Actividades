from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('<int:nota_id>/', views.detalle_nota, name='detalle_nota'),
    path('nueva/', views.crear_nota, name='crear_nota'),
    path('<int:nota_id>/edita/', views.editar_nota, name='editar_nota'),
    path('<int:nota_id>/elimina/', views.eliminar_nota, name='eliminar_nota'),
]