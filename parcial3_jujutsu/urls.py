from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jujutsu.urls')),  # Esto le dice a Django que busque las rutas dentro de la app
]