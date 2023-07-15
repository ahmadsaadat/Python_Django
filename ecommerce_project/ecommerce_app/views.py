from django.shortcuts import render
from .models import Product, Category, Tag
from django.core.paginator import Paginator

def main(request):
    # Set up pagination
    p = Paginator(Product.objects.all(), 4)
    page = request.GET.get('page')
    products = p.get_page(page)

    categories = Category.objects.all()
    tags = Tag.objects.all()

    response = {
        'products':products, 
        'categories': categories,
        'tags': tags
        }

    return render(request, 'main.html', response)
