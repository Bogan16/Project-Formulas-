from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Formula(models.Model):
    text = models.TextField()
    formulas = models.TextField(default='')
    photo_formulas = models.ImageField(upload_to='photos/', null=True, blank=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text
    
