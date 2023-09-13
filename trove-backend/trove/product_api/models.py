from django.db import models
import eav
import uuid

class Category(models.Model):
    name = models.CharField(max_length=150)    

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
    name = models.CharField(max_length=150)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)
    categories = models.ManyToManyField(Category, related_name='products')    
    
    def __str__(self):
        return self.name
    


eav.register(Product)