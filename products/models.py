from django.db import models
from django.conf import settings


class Product(models.Model):
    product_title = models.CharField(max_length=150, null=False)
    product_content = models.TextField(null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(upload_to='media/product/', null=False)
    views = models.IntegerField(default=0, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class WishList(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)