from django.contrib import admin
from products.models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'product_price', 'created_at', 'updated_at')
    search_fields = ('product_title', 'product_content')
