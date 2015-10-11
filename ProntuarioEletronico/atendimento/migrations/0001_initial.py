# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coren', models.IntegerField()),
                ('especialidade', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('matricula', models.IntegerField(max_length=20)),
                ('nome', models.CharField(max_length=100)),
                ('dataAdmissao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HorarioMedicamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horaMedicamento', models.CharField(max_length=10, verbose_name=b'Horario da Medicacao')),
                ('descricaoMedicamento', models.CharField(max_length=30, verbose_name=b'Descricao do Medicamento')),
                ('dosagem', models.CharField(max_length=10)),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.PositiveIntegerField(max_length=11)),
                ('cartao_SUS', models.IntegerField(serialize=False, primary_key=True)),
                ('data_Nascimento', models.DateField()),
                ('sexo', models.CharField(max_length=20, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino')])),
                ('estadoCivil', models.CharField(max_length=20, verbose_name=b'Estado Civil', choices=[('solteiro', 'Solteiro'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('viuvo', 'Viuvo')])),
            ],
        ),
        migrations.CreateModel(
            name='Prontuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo_Prontuario', models.IntegerField(max_length=100)),
                ('data_Consulta', models.DateField()),
            ],
        ),
    ]
