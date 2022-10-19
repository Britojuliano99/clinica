from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Planos(models.Model):
    nome=models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    nome=models.CharField(max_length=100)
    especialidade=models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Paciente(models.Model):

    nome=models.CharField(max_length=100,unique=True)
    Plano=models.ForeignKey(Planos, on_delete=models.CASCADE)
    data_nascimento=models.DateField()
    profissional=models.ForeignKey(Profissional,on_delete=models.CASCADE,blank=True)
    email=models.EmailField(blank=True)
    telefone=models.CharField(max_length=15,blank=True)
    cpf=models.CharField(max_length=11,blank=True)
    carteira_plano=models.CharField(max_length=30,blank=True)
    def __str__(self):
        return self.nome
    def idade(self):
        return datetime.year(timezone.now()-self.data_nascimento)
    
class Sala(models.Model):
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return str(self.id)

class Horarios(models.Model):
    id = models.BigAutoField(primary_key=True)
    horario=models.TimeField()

    def __str__(self):
        return str(self.horario)
class Consulta(models.Model):
    situacoes=(("PC","Pendente Confirmação"),("C","Confirmado"),
    ("F","Falta"),("FJ","Falta Justificada"),("P","Presença"),
    ("R","Reposição"))
    paciente=models.ForeignKey(Paciente,on_delete=models.CASCADE,default=" ")
    dia=models.DateField(default=timezone.now())
    situação=models.CharField(max_length=10,choices=situacoes)
    sala=models.ForeignKey(Sala,on_delete=models.CASCADE)
    horario=models.ForeignKey(Horarios,on_delete=models.CASCADE)

    class Meta:
        constraints=[models.UniqueConstraint(
                fields=["sala","horario","dia"],
                name="Atendimento_unico"
            )
        ]
    def __str__(self):
        return f"Atendimento de {self.paciente} com {self.paciente.profissional}"


    