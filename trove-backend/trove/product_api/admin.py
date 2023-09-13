from django.contrib import admin
from .models import Category, Product
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

class ProductAdminForm(BaseDynamicEntityForm):
    model = Product

class ProductAdmin(BaseEntityAdmin):
    form = ProductAdminForm


admin.site.register(Category)
admin.site.register(Product)
