from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image
from django.shortcuts import reverse

User = get_user_model()

# Create your models here.
class AnimalsType(models.Model):

    slug = models.SlugField(unique=True)
    typeName = models.CharField(max_length=255, verbose_name='Вид животного')
    typeImage = models.FileField(blank=True, null=True, verbose_name='Изображение')
    
    def __str__(self):
        return self.typeName

    def get_absolute_url(self):
        return reverse('category', kwargs={'f_slug': self.slug})

class Animal(models.Model):

    slug = models.SlugField(unique=True)
    animalsType = models.ForeignKey(AnimalsType, on_delete=models.CASCADE, verbose_name='Вид животного')
    available = models.BooleanField(max_length=255, verbose_name='Доступен для покупки', default=True)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Владелец')
    veterinar = models.ForeignKey('Veterinar', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ветеринар')
    veterenaryClinic = models.ForeignKey('VeteranaryClinic',on_delete=models.CASCADE, blank=True, null=True, verbose_name='Ветлечебница')
    nickname = models.CharField(max_length=255, verbose_name='Кличка')
    gender = models.CharField(max_length=255, verbose_name='Пол')
    age = models.CharField(max_length=255 ,verbose_name='Возраст')
    woolCover = models.CharField(max_length=255, verbose_name='Шерстяной покров')
    woolCover = models.CharField(max_length=255, verbose_name='Шерстяной покров')
    woolColor = models.CharField(max_length=255, verbose_name='Цвет шерсти')
    breed = models.CharField(max_length=255, verbose_name='Порода')
    eyesColor = models.CharField(max_length=255, verbose_name='Цвет глаз')
    toilet = models.BooleanField(verbose_name='Приученность к туалету')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    body = models.CharField(max_length=255, verbose_name='Телосложение')
    foodType = models.CharField(max_length=255, verbose_name='Тип питания')
    shortDescriptions = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    advDescriptions = models.TextField(null=True, blank=True, verbose_name='Дополнительное описание')
    main_image = models.ImageField(blank=True, null=True, verbose_name='Изображение на главном экране')
    
    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('animal', kwargs={'f_slug': self.animalsType.slug, 'cur_slug': self.slug})

class AnimalPhoto(models.Model):

    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name='Животное')
    image = models.ImageField(blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.animal.nickname

class Owner(models.Model):
    lastName = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    midName = models.CharField(max_length=255, verbose_name='Отчество')
    adress = models.CharField(max_length=255, verbose_name='Адрес')
    phoneNumber = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return "{} {} {}".format(self.lastName, self.name, self.midName)

class VeteranaryClinic(models.Model):
    clinicNumber = models.CharField(max_length=255, verbose_name='Название ветлечебницы')
    adress = models.CharField(max_length=255, verbose_name='Адрес')
    phoneNumber = models.CharField(max_length=20, verbose_name='Номер телефона')

    def __str__(self):
        return self.clinicNumber

class Veterinar(models.Model):
    veteranaryClinic = models.ForeignKey(VeteranaryClinic,on_delete=models.CASCADE, verbose_name='Ветлечебница')
    lastName = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    midName = models.CharField(max_length=255, verbose_name='Отчество')
    dateOfReg = models.DateField(verbose_name='Дата введения в учёт')
    lastVisit = models.DateField(verbose_name='Дата последнего посещения')

    def __str__(self):
        return "{} {} {}".format(self.lastName, self.name, self.midName)


class ProductsType(models.Model):

    slug = models.SlugField(unique=True)
    typeName = models.CharField(max_length=255, verbose_name='Тип продукта')
    typeImage = models.FileField(blank=True, null=True, verbose_name='Изображение')
    
    def __str__(self):
        return self.typeName

    def get_absolute_url(self):
        return reverse('products', kwargs={'f_slug': self.slug})
        
class PetProduct(models.Model):
    slug = models.SlugField(unique=True)
    productType = models.ForeignKey(ProductsType, on_delete=models.CASCADE, verbose_name='Тип товара')
    shortDescriptions = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    advDescriptions = models.TextField(null=True, blank=True, verbose_name='Дополнительное описание')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    main_image = models.ImageField(blank=True, null=True, verbose_name='Изображение на главном экране')
    name = models.CharField(blank=True, null=True, max_length=255, verbose_name='Название')
    count = models.CharField(max_length=255 ,verbose_name='Количество', default=1)
    available = models.BooleanField(max_length=255, verbose_name='Доступен для покупки', default=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cur_product', kwargs={'f_slug': self.productType.slug, 'cur_slug': self.slug})
        
class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    products = models.ManyToManyField(PetProduct, through='CartPetProduct')
    animals = models.ManyToManyField(Animal)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class CartPetProduct(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    petProduct = models.ForeignKey(PetProduct, on_delete=models.CASCADE, verbose_name='Зоотовары')
    productCount = models.PositiveIntegerField(default=1, verbose_name='Количество товара')