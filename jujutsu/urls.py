from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonajeViewSet

# El router genera automáticamente las rutas de la API
router = DefaultRouter()
router.register(r'personajes', PersonajeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]