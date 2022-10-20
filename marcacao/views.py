from django.shortcuts import render
from django.http import HttpResponse
from .forms import CriarConsulta, CriarPaciente
from .models import Consulta, Profissional
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
import datetime 

# Create your views here.
def home(response):
    return render(response,"marcacao/index.html")

def cadastro_paciente(request):
    if request.method == "POST":
        form=CriarPaciente(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Paciente Cadastrado com Sucesso")

    else:
        form=CriarPaciente()
    return render(request,"marcacao/Cadastro_paciente.html",{'form':form})

def criar_consulta(request):
    
    dias=Consulta.objects.dates("dia","day")
    consultas=Consulta.objects.all()
    form=CriarConsulta()
    if request.method == "POST":
        if 'salvar' in request.POST:
            form=CriarConsulta(request.POST)
            if form.is_valid():
                #form.validate_unique()
                form.save()
        else:
            form=CriarConsulta()
        if 'apagar' in request.POST:
            id=request.POST["apagar"]
            Apagar=Consulta.objects.get(id=id)
            print(id)
            Apagar.delete()
    return render(request,"marcacao/Cadastro_sessoes.html",{'form':form,'consultas':consultas,'dias':dias})

def ver_consultas(request):
    try:
        dia_selecionado=request.GET['dia']
        sala_selecionada=request.GET['sala']
        profissional_selecionado=request.GET['profissional']
        print("pegou")
    except:
        dia_selecionado=""
        sala_selecionada=""
        profissional_selecionado=""
        print('não pegou')
    try:
        consultas=Consulta.objects.filter(Q(dia =f"{dia_selecionado}") & Q(sala=sala_selecionada) & Q(paciente__profissional__nome=f"{profissional_selecionado}"))
        dias=[datetime.datetime.strptime(dia_selecionado,'%Y-%m-%d').date()]
        profissionais=Profissional.objects.all()
        print("filtrando")
    except:
        consultas=Consulta.objects.all()
        dias=Consulta.objects.dates("dia","day")
        profissionais=Profissional.objects.all()
        print("sem filtro")
    if request.method == "POST":
        id=request.POST["apagar"]
        Apagar=Consulta.objects.get(id=id)
        Apagar.delete()
    
    
    return render(request,"marcacao/consultas.html",{'consultas':consultas,"dias":dias,"dia_selecionado":dia_selecionado,"profissionais":profissionais})



class update_consulta(UpdateView):
    model=Consulta
    fields=['situação']
    success_url = reverse_lazy(criar_consulta)
