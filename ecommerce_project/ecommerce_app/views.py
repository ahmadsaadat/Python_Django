from django.shortcuts import render
from .models import Product, Category, Tag

def main(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    for tag in tags:
        print(tag)

    response = {
        'products':products, 
        'categories': categories,
        'tags': tags
        }

    return render(request, 'main.html', response)


