from django.urls import path
from ProyectoWeb import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.servicios,name='Servicios'),
]

