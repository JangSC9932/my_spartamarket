from django.db import models


class Product(models.Model):
    product_title = models.CharField(max_length=150, null=False)
    product_content = models.TextField(null=False)
    product_price = models.IntegerField(null=False)
    product_image = models.ImageField(upload_to='media/', null=False)
    views = models.IntegerField(default=0, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


