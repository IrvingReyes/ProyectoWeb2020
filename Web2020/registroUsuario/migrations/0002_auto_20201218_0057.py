# Generated by Django 3.1.4 on 2020-12-18 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registroUsuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Nombre_Completo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Password',
            field=models.CharField(max_length=1024),
        ),
    ]