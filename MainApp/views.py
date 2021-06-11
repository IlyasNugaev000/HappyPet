from django.shortcuts import render
from .models import *
from .forms import OwnerForm
from django.views.generic import View
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

def test_view(request):
    pet_types = AnimalsType.objects.all()
    context = {"pet_types" : pet_types}
    return render(request, "base.html", context)


class CategoryView(View):

    def get(self, request, f_slug):
        pet_types = AnimalsType.objects.all()
        try:
            current_type = None
            if f_slug == "all":
                current_type = "all"
                catalog_elements = Animal.objects.all().filter(available = True)
            elif f_slug == "last":
                current_type = "last"
                catalog_elements = Animal.objects.all().filter(available = True).order_by("-id")[0:5]
            elif f_slug == "toilet":
                current_type = "toilet"
                catalog_elements = Animal.objects.all().filter(available = True).filter(toilet = True)
            else:
                current_type = pet_types.get(slug = f_slug)
                catalog_elements = Animal.objects.all().filter(animalsType = current_type.id, available = True)
        except AnimalsType.DoesNotExist:
            current_type = None
            catalog_elements = Animal.objects.all()
        context = {"pet_types": pet_types, "catalog_elements": catalog_elements, "current_type": current_type}
        return render(request, "ajax.html", context)


class ProductsView(View):

    def get(self, request, f_slug):
        product_types = ProductsType.objects.all()
        try:
            current_type = None
            if f_slug == "all":
                current_type = "all"
                catalog_elements = PetProduct.objects.all().filter(available = True)
            else:
                current_type = product_types.get(slug = f_slug)
                catalog_elements = PetProduct.objects.all().filter(productType = current_type.id, available = True)
        except productType.DoesNotExist:
            current_type = None
            catalog_elements = PetProduct.objects.all()
        context = {"product_types": product_types, "catalog_elements": catalog_elements, "current_type": current_type}
        return render(request, "ajax_products.html", context)


class AnimalView(View):
    def get(self, request, f_slug, cur_slug):
        current_animal = Animal.objects.get(slug = cur_slug)
        photos = AnimalPhoto.objects.filter(animal = current_animal.id)
        vetclinic_info = current_animal.veterenaryClinic
        veter_info = current_animal.veterinar
        
        current_cart = Cart.objects.get(user=request.user)
        if current_animal in current_cart.animals.all():
            isAvailable = False
        else:
            isAvailable = True
        
        context = {"photos": photos, "current_animal": current_animal, "vetclinic_info": vetclinic_info, "veter_info": veter_info, "isAvailable": isAvailable}
        if current_animal.toilet:
            context["toilet"] = "Приучен"
        else:
            context["toilet"] = "Не приучен"
        return render(request, "animal_information_page.html", context)


class ProductView(View):
    def get(self, request, f_slug, cur_slug):
        current_product = PetProduct.objects.get(slug = cur_slug)
        current_cart = Cart.objects.get(user=request.user)
        cartProducts = CartPetProduct.objects.filter(cart=current_cart)
        isAvailable = True
        for cartProduct in cartProducts:
            if cartProduct.petProduct == current_product:
                isAvailable = False
                break
        context = {"current_product": current_product, "isAvailable": isAvailable}
        return render(request, "product_information_page.html", context)


class Purchase(View):

    def get(self, request):
        form = OwnerForm()
        context = {"form": form}
        return render(request, "order.html", context)

    def post(self, request):
        current_cart = Cart.objects.get(user=request.user)
        cartProducts = CartPetProduct.objects.filter(cart=current_cart)
        
        for animal in current_cart.animals.all():
            animal.available = False
            animal.save()
        
        for cartProduct in cartProducts:
            cartProduct.petProduct.count = str(int(cartProduct.petProduct.count) - cartProduct.productCount)
            if (cartProduct.petProduct.count == "0"):
                cartProduct.petProduct.available = False
            cartProduct.petProduct.save()
        
        current_cart.delete()
        current_cart = Cart()
        current_cart.user = request.user
        current_cart.save()
       
        return HttpResponseRedirect(reverse('category', args=('all',)))
        
class CartView(View):
    def get(self, request, *args, **kwargs):
        current_cart = Cart.objects.get(user=request.user)
        animals = current_cart.animals.all()
        products = CartPetProduct.objects.filter(cart=current_cart)
        
        final_price = 0
        for item in animals:
            final_price+=item.price
        
        for item in products:
            final_price+=item.productCount * item.petProduct.price
            
        context = {
            'animals': animals,
            'products': products,
            'final_price': final_price
        }
        return render(request, 'cart.html', context)

class CartAddingView(View):
    def get(self, request, productType, cur_slug):
        if request.user.is_authenticated:
            current_cart = Cart.objects.get(user=request.user)
                
            if (productType == "animal"):
                current_product = Animal.objects.get(slug = cur_slug)
                current_cart.animals.add(current_product)
            else:
                current_product = PetProduct.objects.get(slug = cur_slug)
                cpp = CartPetProduct(cart=current_cart, petProduct=current_product)
                cpp.save()
                current_cart.products.add(current_product)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        
class AddCount(View):
    @csrf_exempt
    def post(self, request):
        if request.is_ajax():
            idProduct = request.POST['id']
            current_product = PetProduct.objects.get(id = idProduct)
            coll = CartPetProduct.objects.filter(petProduct=current_product)
            for col in coll:
                col.productCount = request.POST['count']
                col.save()
            return JsonResponse({'message': 'OK'})
            
            
class DeleteProduct(View):
    def get(self, request, product):
        current_cart = Cart.objects.get(user=request.user)
        produc = PetProduct.objects.get(id=product)
        cpp = CartPetProduct.objects.get(cart=current_cart, petProduct=produc)
        cpp.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
class DeleteAnimal(View):
    def get(self, request, animal):
        anima = Animal.objects.get(id=animal)
        current_cart = Cart.objects.get(user=request.user)
        current_cart.animals.remove(anima)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

