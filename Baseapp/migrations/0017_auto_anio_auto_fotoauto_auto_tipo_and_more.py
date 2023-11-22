# Generated by Django 4.1.2 on 2023-11-21 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baseapp', '0016_userextension_user_alter_userextension_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='anio',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='fotoauto',
            field=models.ImageField(blank=True, null=True, upload_to='autos/'),
        ),
        migrations.AddField(
            model_name='auto',
            name='tipo',
            field=models.CharField(choices=[('sedan', 'Sedan'), ('Pick-up', 'Pick-up'), ('camion', 'Camion'), ('moto', 'Moto'), ('tractor', 'Tractor'), ('plataforma', 'Plataforma')], default='Sedan', max_length=15),
        ),
        migrations.AlterField(
            model_name='auto',
            name='kilometraje',
            field=models.IntegerField(null=True),
        ),
    ]
