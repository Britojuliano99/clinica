from django import forms
from .models import Paciente,Consulta
class CriarPaciente(forms.ModelForm):
   class Meta:
        model=Paciente
        fields= '__all__'

class CriarConsulta(forms.ModelForm):
   class Meta:
        model=Consulta
        fields= '__all__'
        