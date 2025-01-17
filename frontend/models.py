from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from djrichtextfield.models import RichTextField
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    



    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    poster = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    expected_sales_date = models.DateField()
    thumbnail = models.ImageField(upload_to= 'product_images', null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    status = models.BooleanField(default=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
   
    


 

    def __str__(self):
        return self.product_name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    image = models.ImageField(upload_to= 'product_images', null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name





class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits= 15, decimal_places=2)
    date_bided = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bid)


