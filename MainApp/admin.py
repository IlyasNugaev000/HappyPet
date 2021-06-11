from django.contrib import admin
from django import forms
from django.core.files.base import ContentFile

from .models import *

class AnimalForms(forms.ModelForm):
    photos = forms.ImageField(label=u'Фотографии', required=False, widget=forms.FileInput(attrs={'multiple': 'multiple'}))
    class Meta:
        model = Animal
        fields = "__all__"

class AnimalAdmin(admin.ModelAdmin):
    form = AnimalForms

    def save_model(self, request, obj, form, change):
        if request.method == 'POST':
            for f in request.FILES.getlist('photos'):
                data = f.read()
                photo = AnimalPhoto(animal = obj)
                photo.image.save(f.name, ContentFile(data))
                photo.save()
        obj.save()




# Register your models here.

admin.site.register(AnimalsType)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalPhoto)
admin.site.register(Owner)
admin.site.register(VeteranaryClinic)
admin.site.register(Veterinar)
admin.site.register(PetProduct)
admin.site.register(ProductsType)
admin.site.register(Cart)
admin.site.register(CartPetProduct)