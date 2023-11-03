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
    description = models.TextField(default='')        
    categories = models.ManyToManyField(Category, related_name='products')        
    
    def __str__(self):
        return self.name
    

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=2000)    
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.image_url

eav.register(Product)