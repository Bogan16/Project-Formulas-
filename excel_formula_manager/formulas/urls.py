from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_formula, name='create_formula'),
    path('edit/<slug:slug>/', views.edit_formula, name='edit_formula'),
    path('delete/<slug:slug>/', views.delete_formula, name='delete_formula'),
    path('sort/', views.sort_formulas, name='sort_formulas'),
    path('category/create/', views.create_category, name='create_category'),
    path('category/edit/<str:category_name>/', views.edit_category, name='edit_category'),
    path('category/delete/<str:category_name>/', views.delete_category, name='delete_category'),
]
