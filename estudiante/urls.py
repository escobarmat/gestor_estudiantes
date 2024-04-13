
from django.urls import path
from .views import *

urlpatterns = [
    path('curso/', estudiantes_curso, name='estudiantes_curso'),
    path('mayores/<int:edad>/', estudiantes_mayores, name='estudiantes_mayores'),
    path('cursos/<str:curso>/', cursos, name='cursos'),
    path('', index, name='index'),
]

