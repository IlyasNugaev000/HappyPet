# Generated by Django 3.1.2 on 2020-11-13 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_auto_20201113_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='shortDescriptions',
            field=models.TextField(blank=True, null=True, verbose_name='Краткое описание'),
        ),
    ]
