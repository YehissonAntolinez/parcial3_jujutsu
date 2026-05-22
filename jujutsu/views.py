from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
from .models import Personaje
from .serializers import PersonajeSerializer

# 1. Configuración de la paginación con los parámetros exactos de la rúbrica
class ParcialPagination(PageNumberPagination):
    page_size = 3  # Tamaño por defecto si no se pasa el parámetro
    page_query_param = 'page'  # Parámetro para la página (ej: ?page=1)
    page_size_query_param = 'page_size'  # <--- CORREGIDO: Ahora acepta ?page_size=3
    max_page_size = 100

# 2. Configuración de los filtros avanzados
class PersonajeFilter(filters.FilterSet):
    # Permite buscar por coincidencia parcial en el nombre (ej: ?nombre=gojo)
    nombre = filters.CharFilter(field_name='nombre_personaje', lookup_expr='icontains')
    
    # Filtros numéricos de rango (ej: ?max_energia=50000)
    max_energia = filters.NumberFilter(field_name='energia_maldita', lookup_expr='lte')
    min_energia = filters.NumberFilter(field_name='energia_maldita', lookup_expr='gte')

    class Meta:
        model = Personaje
        fields = ['nombre', 'max_energia', 'min_energia', 'bando', 'grado_rango', 'posee_expansion_dominio']

# 3. Vista principal del proyecto
class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    pagination_class = ParcialPagination
    
    # Inyección de filtros y ordenamientos
    filterset_class = PersonajeFilter
    ordering_fields = ['nombre_personaje', 'energia_maldita']