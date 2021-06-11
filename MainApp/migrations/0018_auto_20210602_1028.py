# Generated by Django 3.1.2 on 2021-06-02 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0017_auto_20201214_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая цена')),
                ('in_order', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('typeName', models.CharField(max_length=255, verbose_name='Тип продукта')),
                ('typeImage', models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
        ),
        migrations.CreateModel(
            name='PetProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('shortDescriptions', models.TextField(blank=True, null=True, verbose_name='Краткое описание')),
                ('advDescriptions', models.TextField(blank=True, null=True, verbose_name='Дополнительное описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение на главном экране')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.cart', verbose_name='Корзина')),
                ('productType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.animalstype', verbose_name='Вид животного')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.cart', verbose_name='Корзина'),
        ),
    ]