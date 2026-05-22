from rest_framework import serializers
from .models import Personaje

class PersonajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personaje
        fields = '__all__'  # Esto incluye automáticamente ID, nombre_personaje, bando, energía, etc.