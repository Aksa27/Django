from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name='base'),
    path('add/',views.add_item,name='add'),
    path('view/',views.view_item,name='view'),
    path('edit/<int:p>',views.edit_item,name='edit'),
    path('delete/<int:p>',views.delete_item,name='delete'),


]
