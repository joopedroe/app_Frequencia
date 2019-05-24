from django.contrib import admin
from .models import *

@admin.register(Config_horario)
class Config_horarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass

@admin.register(status)
class statusAdmin(admin.ModelAdmin):
    pass

@admin.register(Frequencia)
class FrequenciaAdmin(admin.ModelAdmin):
    pass

@admin.register(Justificativa)
class JustificativaAdmin(admin.ModelAdmin):
    pass
# Register your models here.

