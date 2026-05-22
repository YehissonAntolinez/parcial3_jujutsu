from django.db import models

class Personaje(models.Model):
    # Atributos base requeridos por la tabla del parcial
    nombre_personaje = models.CharField(max_length=100)  # Varchar (100)
    descripcion = models.CharField(max_length=300)       # Varchar (300)
    imagen = models.URLField(max_length=500)            # URL del link de la foto
    fecha_creacion = models.DateField(auto_now_add=True) # Date (se guarda solo al crear)

    # Los 4 atributos personalizados del tema (Jujutsu Kaisen)
    bando = models.CharField(max_length=50)                  # Hechicero, Maldición, etc.
    grado_rango = models.CharField(max_length=50)            # Grado Especial, Grado 1, etc.
    energia_maldita = models.IntegerField()                  # Numérico para ordenamiento
    posee_expansion_dominio = models.BooleanField(default=False) # Booleano para filtros

    def __str__(self):
        return self.nombre_personaje

    # Clase Meta para corregir la paginación y ordenar por defecto
    class Meta:
        ordering = ['-fecha_creacion']  # Muestra primero los personajes más nuevos