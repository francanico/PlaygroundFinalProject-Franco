# Generated by Django 4.1.2 on 2023-11-23 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Baseapp', '0020_delete_muro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poliza',
            name='nombre',
        ),
        migrations.AddField(
            model_name='poliza',
            name='users',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
