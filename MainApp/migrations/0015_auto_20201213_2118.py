# Generated by Django 3.1.2 on 2020-12-13 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0014_animal_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cartElements',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='cartelem',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='cartelem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartelem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartElem',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]