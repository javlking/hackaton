from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('about', views.get_about),
    path('products', views.get_product),
    path('contacts', views.get_contact),
    path('<int:pk>', views.get_full_product),
    path('category/<int:pk>', views.get_full_category),
    path('cart', views.get_user_cart),
    path('del_item/<int:pk>', views.delete_item_from_cart),
]