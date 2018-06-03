from django.urls import path
from .views import AllItemsList, FridgeList, TVList

app_name = 'items'

urlpatterns = [
    path("", AllItemsList.as_view(), name="items-list"),
    path("fridges", FridgeList.as_view(), name="fridge-list"),
    path("tv-sets", TVList.as_view(), name="tv-list")
]
