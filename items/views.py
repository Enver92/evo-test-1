from django.shortcuts import render
from django.views.generic import ListView
from .models import Item


# Create your views here.
class AllItemsList(ListView):
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.all()
    template_name = 'items/items.html'


class FridgeList(ListView):
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.filter(category__category='Fridge')
    template_name = 'items/fridge_list.html'


class TVList(ListView):
    model = Item
    context_object_name = 'items'
    queryset = Item.objects.filter(category__category='TV')
    template_name = 'items/tv_list.html'
