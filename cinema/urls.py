from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from applications.page import views
from . import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('/', include('applications.page.urls')),
    path('films/', include('applications.film.urls')),
    path('posters/', include('applications.poster.urls')),
    path('admin/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
