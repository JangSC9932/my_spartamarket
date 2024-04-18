from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.list_products, name='list'),
    path('create/', views.create_product, name='create'),
    path('detail/<int:product_id>/', views.detail_product, name='detail'),
    path('update/<int:product_id>/', views.update_product, name='update'),
    path('delete/<int:product_id>/', views.delete_product, name='delete'),
]