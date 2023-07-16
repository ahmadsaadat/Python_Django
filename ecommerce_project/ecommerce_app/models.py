from django.db import models

class Category(models.Model):
    """
    Category model represents different categories a product can belong to. 

    attributes:
    name - unique, varchar 200 character length
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    """
    Tag model represents various tags that can be associated with a product. 

    attributes:
    name = unique, varchar 200 character length
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    """
    Product model represents the items or goods. 
    
    attributes: 
    name = unique, varchar 200 character length
    description = textfield
    category = Foreign key, enables product to be deleted if category is deleted 
    tags = Foreign key, enables product to be deleted if tag is deleted
    picture_url = varchar, 1024 character length
    """
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField() 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag) 
    picture_url = models.CharField(max_length=1024)

    def __str__(self):
        return self.name
