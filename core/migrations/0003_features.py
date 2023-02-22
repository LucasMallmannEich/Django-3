# Generated by Django 4.1.7 on 2023-02-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_team_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('data_modificacao', models.DateField(auto_now=True, verbose_name='Data de Modificação')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-leaf', 'Folha'), ('lni-laptop-phone', 'Eletrônicos'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete')], max_length=16, verbose_name='Ícone')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
    ]