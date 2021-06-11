from django.urls import path

from .views import *

urlpatterns = [
    path('', test_view, name="base"),
    path('category/<slug:f_slug>/', CategoryView.as_view(), name='category'),
    path('products/<slug:f_slug>/', ProductsView.as_view(), name='products'),
    path('category/<slug:f_slug>/<slug:cur_slug>/', AnimalView.as_view(), name='animal'),
    path('products/<slug:f_slug>/<slug:cur_slug>/', ProductView.as_view(), name='cur_product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('buy/', Purchase.as_view(), name='purchase'),
    path('cart/<str:productType>/<slug:cur_slug>/', CartAddingView.as_view(), name='cartAdding'),
    path('delete/animal/<str:animal>/', DeleteAnimal.as_view(), name='deleteAnimal'),
    path('delete/<str:product>/', DeleteProduct.as_view(), name='deleteProduct'),
    path('cart/addCount/', AddCount.as_view(), name='addCount'),
    
]