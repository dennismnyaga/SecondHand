from django.db import models
from django.contrib.auth.models import User
import uuid
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    # CATEGORY = (
    #     ('Electronics', 'Electronics'),
    #     ('Furniture', 'Furniture'),
    #     ('Fashion', 'Fashion'),
    #     ('More', 'More'),
    #     ('Prop', 'Prop'),
    #     ('vehicles', 'vehicles')
    # )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    poster = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # category = models.CharField(max_length = 200, choices = CATEGORY)
    category = models.ForeignKey(Category ,on_delete=models.CASCADE, null=True, blank=True)
    expected_sales_date = models.DateField()
    current_bid = models.DecimalField(max_digits=7, decimal_places=2)
    images = models.ImageField(upload_to='product_images', null = True)
    details = models.TextField()
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name



    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.images:
    #         img = Image.open(default_storage.open(self.images.name))
    #         if img.height > 1080 or img.width > 1920:  # pragma:no cover
    #             output_size = (1920, 1080)
    #             img.images(output_size)
    #             buffer = BytesIO()
    #             img.save(buffer, format="JPEG")
    #             default_storage.save(self.images.name, buffer)


class Bid(models.Model):

    user = models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    timestamp = models.DateTimeField( auto_now=True)
    bid = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.ForeignKey(
        Product, verbose_name=("product"), on_delete=models.CASCADE, related_name="comment"
    )

    class Meta:
        verbose_name = ("Bid")
        verbose_name_plural = ("Bids")

    def __str__(self):
        return self.user.username