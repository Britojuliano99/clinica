from django.shortcuts import render
from django.http import HttpResponse
from .forms import CriarConsulta, CriarPaciente
from .models import Consulta, Profissional
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
import datetime

# Create your views here.


def home(request):
    print(request.user.is_authenticated)
    return render(request, "marcacao/index.html",{"user":request.user})


def cadastro_paciente(request):
    if request.method == "POST":
        form = CriarPaciente(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Paciente Cadastrado com Sucesso")

    else:
        form = CriarPaciente()
    return render(request, "marcacao/Cadastro_paciente.html", {'form': form})


def criar_consulta(request):

    dias = Consulta.objects.dates("dia", "day")
    consultas = Consulta.objects.all()
    form = CriarConsulta()
    if request.method == "POST":
        if 'salvar' in request.POST:
            form = CriarConsulta(request.POST)
            if form.is_valid():
                # form.validate_unique()
                form.save()
        else:
            form = CriarConsulta()
        if 'apagar' in request.POST:
            id = request.POST["apagar"]
            Apagar = Consulta.objects.get(id=id)
            print(id)
            Apagar.delete()
    return render(request, "marcacao/Cadastro_sessoes.html", {'form': form, 'consultas': consultas, 'dias': dias})


def ver_consultas(request):
    profissionais = Profissional.objects.all()
    
    
    
    try:
        dia_selecionado = request.GET['dia']
        sala_selecionada = request.GET['sala']
        profissional_selecionado = request.GET['profissional']
        print("pegou")
    except:
        dia_selecionado = ""
        sala_selecionada = ""
        profissional_selecionado = ""
        print('não pegou')
    # Todas as opções verdadeiras
    if ((dia_selecionado != "")  and (sala_selecionada != "") and (profissional_selecionado != "")):
            consultas = Consulta.objects.filter(Q(dia=f"{dia_selecionado}") & Q(
                sala=sala_selecionada) & Q(paciente__profissional__nome=f"{profissional_selecionado}"))
            dias = [datetime.datetime.strptime(
                dia_selecionado, '%Y-%m-%d').date()]
            
        
        
    # Apenas sala e profissional
    elif ((dia_selecionado == "") and (sala_selecionada != "") and (profissional_selecionado != "")):
            consultas = Consulta.objects.filter(Q(sala=sala_selecionada) & Q(
                paciente__profissional__nome=f"{profissional_selecionado}"))
            dias = Consulta.objects.filter(paciente__profissional__nome=f"{profissional_selecionado}").dates("dia", "day")
            
       
    # Apenas dia e profissional
    elif ((dia_selecionado != "") and (sala_selecionada == "") and (profissional_selecionado != "")):
            consultas = Consulta.objects.filter(Q(dia=f"{dia_selecionado}") & Q(
                paciente__profissional__nome=f"{profissional_selecionado}"))
            dias = [datetime.datetime.strptime(
                dia_selecionado, '%Y-%m-%d').date()]
    # Apenas dia e sala
    elif ((dia_selecionado != "") and (sala_selecionada != "") and (profissional_selecionado == "")):
        
            consultas = Consulta.objects.filter(
                Q(dia=f"{dia_selecionado}") & Q(sala=sala_selecionada))
            dias = [datetime.datetime.strptime(
                dia_selecionado, '%Y-%m-%d').date()]
    
        
    # Apenas o dia
    elif ((dia_selecionado != "") and (sala_selecionada == "") and (profissional_selecionado == "")):
        
            consultas = Consulta.objects.filter(Q(dia=f"{dia_selecionado}"))
            dias = [datetime.datetime.strptime(
                dia_selecionado, '%Y-%m-%d').date()]
           
        
    # Apenas a sala
    elif ((dia_selecionado == "") and (sala_selecionada != "") and (profissional_selecionado == "")):
            consultas = Consulta.objects.filter(Q(sala=sala_selecionada))
            dias = Consulta.objects.dates("dia", "day")
           
        
    
    # Apenas o profissional
    elif ((dia_selecionado == "") and (sala_selecionada == "") and (profissional_selecionado != "")):
            consultas = Consulta.objects.filter(
                Q(paciente__profissional__nome=f"{profissional_selecionado}"))
            dias = Consulta.objects.filter(paciente__profissional__nome=f"{profissional_selecionado}").dates("dia", "day")
           

    else:
        consultas = Consulta.objects.all()
        dias = Consulta.objects.dates("dia", "day")
        

    if request.method == "POST":
        id = request.POST["apagar"]
        Apagar = Consulta.objects.get(id=id)
        Apagar.delete()

    return render(request, "marcacao/consultas.html", {'consultas': consultas, "dias": dias, "dia_selecionado": dia_selecionado, "profissionais": profissionais})


class update_consulta(UpdateView):
    model = Consulta
    fields = ['situação']
    success_url = reverse_lazy(criar_consulta)
