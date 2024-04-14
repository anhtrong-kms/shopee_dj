from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

def index(request):
    # Lấy danh sách sản phẩm từ database
    products = Product.objects.all()

    # Lấy danh sách các danh mục từ database
    categories = Category.objects.all()

    # Truyền danh sách sản phẩm và danh sách danh mục vào template HTML
    return render(request, 'pages/home.html', {'products': products, 'categories': categories})

def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator (product_list, 16)

    page_number = request.GET.get("page_number")

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        products = paginator.page(paginator.num_pages)
    return render(request, "home.html", {"products": products})