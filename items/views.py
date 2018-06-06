from django.shortcuts import HttpResponse
from django.views.generic import ListView
from .models import Item
from django.db.models import F
from django.core import serializers


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


def clickCount(request):
    item_id = None
    if request.method == "GET":
        item_id = request.GET['item_id']

    item = Item.objects.get(id=item_id)
    if item:
        clicks = item.number_of_clicks + 1
        item.number_of_clicks = clicks
        item.save()

    return HttpResponse(clicks)



    # if request.is_ajax():
    #     item_id = request.POST.get('item_id')
    #     item = Item.objects.get(id=item_id)
    #     print(item)
    #     item.number_of_clicks = F("number_of_clicks") + 1
    #     item.save()
    #     item.refresh_from_db()
    #     print("****************************************")
    #     response = serializers.serialize('json', list(item.number_of_clicks,), fields=('click'))
    #
    #     return HttpResponse(response, mimetype='application/json')
