from django.contrib import admin
from .models import Category, Formula

class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

class FormulaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Formula._meta.fields]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Formula, FormulaAdmin)