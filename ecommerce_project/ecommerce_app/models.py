from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=False) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    tags = models.ManyToManyField(Tag) 
    picture_url = models.URLField(max_length=500, null=True, blank=False)

    def __str__(self):
        return self.name
