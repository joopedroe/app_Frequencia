# Generated by Django 2.1.7 on 2019-05-24 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_ponto', '0004_auto_20190511_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='frequencia',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_ponto.status'),
        ),
    ]