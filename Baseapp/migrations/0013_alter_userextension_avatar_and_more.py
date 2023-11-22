# Generated by Django 4.1.2 on 2023-11-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baseapp', '0012_remove_userextension_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='avatar',
            field=models.ImageField(blank=True, default='blank-profile.png', null=True, upload_to='avatares/', verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='userextension',
            name='link',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='link'),
        ),
    ]
