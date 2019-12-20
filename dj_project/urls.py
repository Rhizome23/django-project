from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('storage_app/',include('django.contrib.auth.urls')),
    path('', include('storage_app.urls')),

]
