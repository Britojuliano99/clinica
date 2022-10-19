from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
# Create your views here.
def register(response):
    
    if response.method == "POST":
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.validate_unique()
            form.save()
            return HttpResponse("Usuario Cadastrado com sucesso")
        else:
            return HttpResponse("Erro")
    else:
        form=UserCreationForm()
    return render(response,"register/Cadastrar.html",{"form":form})

