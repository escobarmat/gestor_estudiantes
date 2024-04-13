from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    horas_dictado = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField()
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, related_name='estudiantes', null=True)
    nota_curso = models.IntegerField()

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre



