# Generated by Django 3.1.2 on 2020-11-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_animal_foodtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='foodType',
            field=models.CharField(max_length=255, verbose_name='Тип питания'),
        ),
    ]
