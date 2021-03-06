# Generated by Django 4.0.4 on 2022-04-19 19:30

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=200)),
                ('image', cloudinary.models.CloudinaryField(default=True, max_length=255, verbose_name='image')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
