from rest_framework import serializers
from .models import Aluno, Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    curso_id = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all(),
        source="curso",
        write_only=True
    )

    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'email', 'curso', 'curso_id']
