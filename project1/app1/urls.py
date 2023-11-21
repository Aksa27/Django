from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name='base'),
    path('add/',views.add_item,name='add'),
    path('view/',views.view_item,name='view'),


]
