from django.urls import path

from foodTracker import views

app_name = 'foodTracker'

urlpatterns = [
    path('', views.index, name = 'index')
]