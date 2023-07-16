from django.shortcuts import render
from .models import Product, Category, Tag
from django.core.paginator import Paginator

def main(request):
    """
    A view function serving the main application page.

    It fetches GET parameters from the request for product filtering and pagination.
    Query optimization is done using `select_related` and `prefetch_related` methods.

    Parameters:
    request (HttpRequest): The incoming HTTP request.

    Returns:
    HttpResponse: The rendered 'main.html' template.
    """

    # Extract search and filter parameters from request
    description_search = request.GET.get('description')
    category_filter = request.GET.getlist('category')
    tags_filter = request.GET.getlist('tag')

    # Query products with optimally
    product_list = Product.objects.select_related('category').prefetch_related('tags')

    # Apply filters
    if description_search:
        product_list = product_list.filter(description__icontains=description_search)
    
    if category_filter:
        product_list = product_list.filter(category__name__in=category_filter)

    if tags_filter:
        product_list = product_list.filter(tags__name__in=tags_filter)

    # Set up pagination
    p = Paginator(product_list, 4)
    page = request.GET.get('page')
    products = p.get_page(page)

    # Fetch categories and tags for frontend
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    # Prepare response
    response = {
        'products':products, 
        'categories': categories,
        'tags': tags
        }

    # Render and return the response
    return render(request, 'main.html', response)