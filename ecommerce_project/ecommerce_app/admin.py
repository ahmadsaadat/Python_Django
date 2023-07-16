from django.contrib import admin
from .models import Product, Category, Tag

# Register the models with the admin site. 
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Tag)

