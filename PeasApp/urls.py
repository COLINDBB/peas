from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.show_images, name = 'show image'),
    path('show_images', views.show_images, name = 'show image')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

