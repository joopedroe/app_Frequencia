# Generated by Django 2.1.7 on 2019-05-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_ponto', '0003_frequencia_fucionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='horario_entrada_1',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='horario_entrada_2',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='horario_saida_1',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='frequencia',
            name='horario_saida_2',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
