from django.contrib import admin
from .models import Paciente,Planos,Profissional,Sala,Consulta,Horarios
# Register your models here.

admin.site.register(Paciente)
admin.site.register(Planos)
admin.site.register(Profissional)
admin.site.register(Sala)
admin.site.register(Consulta)
admin.site.register(Horarios)