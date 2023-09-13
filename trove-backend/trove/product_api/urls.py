from django.urls import path
from .views import (get_products, get_product, create_product, update_product, delete_product)

app_name = 'products'

urlpatterns = [
    path('', get_products, name='product-list'),    
    path('', create_product, name='product-create'),    
    path('<uuid:pk>/', get_product, name='product-detail'),
    path('<uuid:pk>/', update_product, name='product-update'),
    path('<uuid:pk>/', delete_product, name='product-delete'),
]