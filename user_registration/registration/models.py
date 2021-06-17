from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Product(models.Model):
    puser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=82)
    price = models.IntegerField(default=0)
    long_description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    

    def get_user_products(self, user):
        return Product.objects.filter(puser=user)
    
    def create_product(self, user, name, s_dec, price, l_dec):
        product = Product.objects.create(puser=user, name=name, short_description= s_dec, price= price, long_description= l_dec)
        product.save()


