# Generated by Django 4.1.2 on 2023-11-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baseapp', '0026_alter_auto_propietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='propietario',
        ),
        migrations.AddField(
            model_name='auto',
            name='emailauto',
            field=models.CharField(default=2, max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
    ]