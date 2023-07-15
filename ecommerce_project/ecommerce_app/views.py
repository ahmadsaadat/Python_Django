from django.shortcuts import render
from .models import Product, Category, Tag
from django.core.paginator import Paginator

def main(request):

    description_search = request.GET.get('description')
    category_filter = request.GET.getlist('category')
    tags_filter = request.GET.getlist('tag')

    product_list = Product.objects.all()

    if description_search:
        print("description_search: ", description_search)
        product_list = product_list.filter(description__icontains=description_search)
    
    if category_filter:
        print("category_filter: ", category_filter)
        product_list = product_list.filter(category__name__in=category_filter)

    if tags_filter:
        print("tags_filter: ", tags_filter)
        product_list = product_list.filter(tags__name__in=tags_filter)

    # Set up pagination
    p = Paginator(product_list, 4)
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
