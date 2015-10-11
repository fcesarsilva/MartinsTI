from django.contrib import admin
from atendimento.models import Paciente
from atendimento.models import Prontuario
from atendimento.models import Funcionario
from atendimento.models import Enfermeiro
from atendimento.models import HorarioMedicamento

admin.site.register(Paciente)
admin.site.register(Prontuario)
admin.site.register(Funcionario)
admin.site.register(Enfermeiro)
admin.site.register(HorarioMedicamento)

# Register your models here.
