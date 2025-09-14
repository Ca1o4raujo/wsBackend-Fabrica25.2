from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Curso
from rest_framework import viewsets
from .serializers import AlunoSerializer, CursoSerializer
from .forms import AlunoForm, CursoForm

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, "academico/cursos_list.html", {"cursos": cursos})

def curso_create(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cursos_list")
    return render(request, "academico/curso_form.html", {"form": form})

def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        return redirect("cursos_list")
    return render(request, "academico/curso_form.html", {"form": form})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == "POST":
        curso.delete()
        return redirect("cursos_list")
    return render(request, "academico/curso_confirm_delete.html", {"curso": curso})

def alunos_list(request):
    alunos = Aluno.objects.select_related("curso").all()
    return render(request, "academico/alunos_list.html", {"alunos": alunos})

def aluno_create(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("alunos_list")
    return render(request, "academico/aluno_form.html", {"form": form})

def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect("alunos_list")
    return render(request, "academico/aluno_form.html", {"form": form})

def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        aluno.delete()
        return redirect("alunos_list")
    return render(request, "academico/aluno_confirm_delete.html", {"aluno": aluno})

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
