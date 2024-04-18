from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .forms import ProductForm
from django.urls import reverse

from .models import Product


# 글 목록
def list_products(request):
    products = Product.objects.all().order_by('-created_at')
    context = {'products': products}
    return render(request, "list.html", context)


# 글 작성
@require_http_methods(['POST', 'GET'])
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                "message": "정상적으로 등록하였습니다.",
                "return_url": f"{reverse('products:list')}"
            }
            return render(request, "message.html", context)
        else:
            return render(request, "create.html", {"form": form})
    else:
        return render(request, "create.html")


# 글 상세
@require_http_methods('GET')
def detail_product(request, product_id):
    context = {
        "product": get_object_or_404(Product, id=product_id)
    }
    return render(request, "detatil.html", context)


# 글 수정
@require_http_methods(['GET', 'POST'])
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            context = {
                "message": "정상적으로 수정하였습니다.",
                "return_url": f"{reverse('products:detail', kwargs={'product_id': product_id})}"
            }
            return render(request, "message.html", context)
        else:
            context = {
                "product": product,
                "form": form
            }
            return render(request, "update.html", context)
    else:
        context = {
            "product": product
        }
        return render(request, "update.html", context)


# 글 삭제
def delete_product(request, product_id):
    get_object_or_404(Product, id=product_id).delete()
    context = {
        "message": "정상적으로 삭제하였습니다.",
        "return_url": f"{reverse('products:list')}"
    }
    return render(request, "message.html", context)