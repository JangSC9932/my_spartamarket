from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.list_products, name='list'),
    path('create/', views.create_product, name='create'),
    path('detail/<int:product_id>/', views.detail_product, name='detail'),
    path('update/<int:product_id>/', views.update_product, name='update'),
    path('delete/<int:product_id>/', views.delete_product, name='delete'),
    path('wishlist_add/<int:product_id>/', views.product_wishlist_add, name='wishlist_add'),
    path('wishlist_remove/<int:product_id>/', views.product_wishlist_remove, name='wishlist_remove'),
    path('wishlist/', views.product_wishlist, name='wishlist'),

]