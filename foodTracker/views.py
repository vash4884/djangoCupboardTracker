from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from foodTracker.models import FoodItem
from django.template import loader
# Create your views here.


def index(request):
    data = FoodItem.objects.all().values()
    template = loader.get_template('index.html')
    context = {'data': data}

    return HttpResponse(template.render(context, request))

def addFood(request):

    food, created = FoodItem.objects.update_or_create(
    name="Colby Cheese Slices",
    food_type="Cheese",
    amount_on_hand=16,
    )
    return redirect('index')
    #return render(request, 'addFood.html', )


def deleteFood(request,id =None):
    item = get_object_or_404(FoodItem, id=id)
    item.delete()
    return redirect('index')