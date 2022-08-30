from django.urls import path
from . import views

# Создаем свои адреса
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contacts', views.contacts),
    path('product/<str:pk>', views.about_product),
    path('cart', views.user_cart),
    path('add_product/<int:pk>', views.add_pr_to_cart),
    path('del_item/<int:pk>', views.delete_from_cart),
    path('send_to_tg/<int:pk>', views.confirm_order),
]
