from django.contrib import admin
from .models import Category, Item, Manufacturer, ItemImage
# Register your models here.

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Manufacturer)
admin.site.register(ItemImage)
