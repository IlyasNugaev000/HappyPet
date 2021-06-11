# Generated by Django 3.1.2 on 2021-06-02 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_auto_20210602_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='petproduct',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='petproduct',
            name='productType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.productstype', verbose_name='Тип товара'),
        ),
    ]
