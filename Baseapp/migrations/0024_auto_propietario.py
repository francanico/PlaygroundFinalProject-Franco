# Generated by Django 4.1.2 on 2023-11-23 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baseapp', '0023_alter_poliza_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='propietario',
            field=models.CharField(default=1, max_length=50, verbose_name='Propietario'),
            preserve_default=False,
        ),
    ]