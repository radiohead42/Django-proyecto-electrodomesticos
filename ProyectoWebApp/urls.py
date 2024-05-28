from django.urls import path
from ProyectoWeb import settings
from ProyectoWebApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='Home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)