from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.urls import reverse

from .models import Product, WishList


# 글 목록
def list_products(request):
    products = Product.objects.all().order_by('-created_at')
    context = {'products': products}
    return render(request, "products/list.html", context)


# 글 작성
@require_http_methods(['POST', 'GET'])
@login_required()
def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            context = {
                "message": "정상적으로 등록하였습니다.",
                "return_url": f"{reverse('products:list')}"
            }
            return render(request, "message.html", context)
        else:
            return render(request, "products/create.html", {"form": form})
    else:
        return render(request, "products/create.html")


# 글 상세
@require_http_methods('GET')
def detail_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.views += 1
    product.save()
    context = {
        "product": get_object_or_404(Product, id=product_id),
        "is_wishing": WishList.objects.filter(product=product, author=request.user).exists()
    }
    return render(request, "products/detail.html", context)


# 글 수정
@require_http_methods(['GET', 'POST'])
@login_required()
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.author != request.user:
        return render(request, "message.html", {"message": "작성자가 아닙니다.", "return_url": reverse("products:list")})

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
            return render(request, "products/update.html", context)
    else:
        context = {
            "product": product
        }
        return render(request, "products/update.html", context)


# 글 삭제
@login_required()
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.author != request.user:
        return render(request, "message.html", {"message": "작성자가 아닙니다.","return_url": reverse("products:list")})

    product.delete()
    context = {
        "message": "정상적으로 삭제하였습니다.",
        "return_url": f"{reverse('products:list')}"
    }

    return render(request, "message.html", context)


# 글 찜하기
@login_required
@require_http_methods(["POST"])
def product_wishlist_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        if product.author != request.user:
            if not WishList.objects.filter(product=product, author=request.user).exists():
                wishlist = WishList()
                wishlist.product = product
                wishlist.author = request.user
                wishlist.save()
                return redirect("products:detail", product_id)
    return redirect("products:detail", product_id)


@login_required
@require_http_methods(["POST"])
def product_wishlist_remove(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        if product.author != request.user:
            wishlist = WishList.objects.filter(product=product, author=request.user)
            if wishlist.exists():
                wishlist.delete()
                return redirect("products:detail", product_id)
    return redirect("products:detail", product_id)


@login_required
@require_http_methods(["GET"])
def product_wishlist(request):
    wishlist = WishList.objects.filter(author=request.user).all()
    context = {
        "wishlist": wishlist
    }
    return render(request, "products/my_list.html", context)
