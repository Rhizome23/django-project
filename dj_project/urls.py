from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('storage_app/',include('django.contrib.auth.urls')),
    path('', include('storage_app.urls')),
    path('',include('ckeditor_uploader.urls')),
]
