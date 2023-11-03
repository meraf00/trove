from django.urls import path
from .views import products_create_list, product_detail_update_delete

app_name = "products"

urlpatterns = [
    path("", products_create_list, name="product-list"),
    path("<uuid:pk>/", product_detail_update_delete, name="product-detail"),
]
