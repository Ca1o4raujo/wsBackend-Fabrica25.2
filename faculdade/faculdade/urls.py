from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from academico.views import (
    alunos_list, aluno_create, aluno_update, aluno_delete,
    cursos_list, curso_create, curso_update, curso_delete, 
    universidades_list, UniversidadesAPI,
    AlunoViewSet, CursoViewSet
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('alunos/', alunos_list, name="alunos_list"),
    path('alunos/novo/', aluno_create, name="aluno_create"),
    path('alunos/<int:pk>/editar/', aluno_update, name="aluno_update"),
    path('alunos/<int:pk>/deletar/', aluno_delete, name="aluno_delete"),
    path('universidades/', universidades_list, name="universidades_list"),
    
    path('cursos/', cursos_list, name="cursos_list"),
    path('cursos/novo/', curso_create, name="curso_create"),
    path('cursos/<int:pk>/editar/', curso_update, name="curso_update"),
    path('cursos/<int:pk>/deletar/', curso_delete, name="curso_delete"),
    
    path('api/', include(router.urls)),
    path('api/universidades/', UniversidadesAPI.as_view(), name="universidades_api"),
]
