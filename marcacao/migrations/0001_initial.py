# Generated by Django 4.1.1 on 2022-10-17 17:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especialidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('data_nascimento', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('cpf', models.CharField(blank=True, max_length=11)),
                ('carteira_plano', models.CharField(blank=True, max_length=30)),
                ('Plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcacao.planos')),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcacao.profissional')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(default=datetime.datetime(2022, 10, 17, 17, 3, 2, 863415, tzinfo=datetime.timezone.utc))),
                ('situação', models.CharField(choices=[('PC', 'Pendente Confirmação'), ('C', 'Confirmado'), ('F', 'Falta'), ('FJ', 'Falta Justificada'), ('P', 'Presença'), ('R', 'Reposição')], max_length=10)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcacao.horarios')),
                ('paciente', models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='marcacao.paciente')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcacao.sala')),
            ],
        ),
        migrations.AddConstraint(
            model_name='consulta',
            constraint=models.UniqueConstraint(fields=('sala', 'horario', 'dia'), name='Atendimento_unico'),
        ),
    ]