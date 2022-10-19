from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Cadastro_paciente/', views.cadastro_paciente, name='cadastro_paciente'),
    path('Cadastro_sessoes/', views.criar_consulta, name='cadastro_sessões'),
    path('Consultas/',views.ver_consultas,name="Visualizar consultas como função"),
    path('Consultas/editar/<int:pk>', views.update_consulta.as_view(), name='consulta editar')
]