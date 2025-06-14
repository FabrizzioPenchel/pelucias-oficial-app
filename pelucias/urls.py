from django.urls import path
from . import views

app_name = 'pelucias'

urlpatterns = [
    path('', views.lista_pelucias, name='lista_pelucias'),
]