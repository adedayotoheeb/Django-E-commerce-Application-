from unicodedata import category
from django.shortcuts import render, get_object_or_404

from .models import Category, Product

# Create your views here.


def index(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        "products": products,
    }
    return render(request, 'store/index.html', context)


def dashboard(request):
    return render(request, 'store/dashboard.html')


def register(request):
    return render(request, 'store/register.html')


def search(request):
    return render(request, 'store/search-result.html')


def signin(request):
    return render(request, 'store/signin.html')


def order(request):
    return render(request, 'store/order_complete.html')


def product_detail(request, category_slug, product_slug):
    try:
        single_product = get_object_or_404(Product,
                                           category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context = {
        "single_product": single_product,
    }
    return render(request, 'store/product-detail.html', context)


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)
        product_count = products.count()
    else:

        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        "products": products,
        "products_count": product_count
    }
    return render(request, 'store/store.html', context)
