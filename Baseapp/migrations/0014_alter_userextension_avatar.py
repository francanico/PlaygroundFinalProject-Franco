# Generated by Django 4.1.2 on 2023-11-21 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baseapp', '0013_alter_userextension_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextension',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatares/', verbose_name='avatar'),
        ),
    ]
