from django.contrib import admin

from core.models import Cargo, Servico, Team, Features


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo', 'ativo', 'data_criacao', 'data_modificacao']


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['servico', 'descricao', 'icone', 'ativo', 'data_criacao', 'data_modificacao']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'bio', 'imagem', 'ativo', 'data_criacao', 'data_modificacao']


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'icone', 'ativo', 'data_criacao', 'data_modificacao']