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
    price = models.DecimalField(max_digits=7, decimal_places=2)
    expected_sales_date = models.DateField()
    thumbnail = models.ImageField(upload_to= 'product_images', null=False, blank=False)
    current_bid = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
   
    


 

    def __str__(self):
        return self.product_name


class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    image = models.ImageField(upload_to= 'product_images', null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.products.product_name





class Bid(models.Model):

    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.ForeignKey(
        Product, verbose_name=("product"), on_delete=models.CASCADE, related_name="comment"
    )

    class Meta:
        verbose_name = ("Bid")
        verbose_name_plural = ("Bids")

    def __str__(self):
        return self.user.username



