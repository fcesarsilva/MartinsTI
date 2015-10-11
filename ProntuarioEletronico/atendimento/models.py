from django.db import models

class Paciente(models.Model):

        SEXO_CHOICES = (

                (u'masculino', u'Masculino'),
                (u'feminino', u'Feminino'),

        )

        ESTADO_CIVIL_CHOICES = (

                (u'solteiro', u'Solteiro'),
                (u'casado', u'Casado'),
                (u'divorciado', u'Divorciado'),
                (u'viuvo', u'Viuvo'),

        )


        #apelido = models.CharField(max_length = 30)
        nome = models.CharField(max_length = 100)
        cpf = models.PositiveIntegerField(max_length = 11)
        cartao_SUS = models.IntegerField(primary_key = True)
        data_Nascimento = models.DateField()
        sexo = models.CharField(max_length = 20, choices = SEXO_CHOICES)
        estadoCivil = models.CharField(max_length = 20, choices = ESTADO_CIVIL_CHOICES, verbose_name = 'Estado Civil')

class Prontuario(models.Model):
        codigo_Prontuario = models.IntegerField(max_length = 100)
        data_Consulta = models.DateField()

class Funcionario(models.Model):
	matricula = models.IntegerField(max_length = 20)
        nome = models.CharField(max_length=100)
        dataAdmissao = models.DateField()

class Enfermeiro(models.Model):
		coren = models.IntegerField()
		especialidade = models.CharField(max_length = 30)

class HorarioMedicamento(models.Model):
		horaMedicamento = models.CharField(max_length = 10, verbose_name = 'Horario da Medicacao')
		descricaoMedicamento = models.CharField(max_length = 30, verbose_name = 'Descricao do Medicamento')
		dosagem = models.CharField(max_length = 10)
		data = models.DateField()
# Create your models here.
