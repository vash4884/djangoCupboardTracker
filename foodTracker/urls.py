from django.template.defaulttags import url
from django.urls import path

from foodTracker import views

app_name = 'foodTracker'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name='index'),
    path('addFood', views.addFood, name ='addFood'),
    path('deleteFood/<str:id>', views.deleteFood, name='deleteFood'),
]