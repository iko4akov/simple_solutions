# Generated by Django 5.0 on 2023-12-07 14:29

import user.service
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=user.service.save_picture, verbose_name='avatar'),
        ),
    ]
