# Generated by Django 3.1.2 on 2020-12-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_auto_20201213_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veteranaryclinic',
            name='clinicNumber',
            field=models.IntegerField(verbose_name='Название ветлечебницы'),
        ),
    ]