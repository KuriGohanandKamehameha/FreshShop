from django.db import models
from django.template.context_processors import request
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(decimal_places=10,max_digits=12)
    image=models.ImageField(upload_to='')

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

