from django.shortcuts import render, get_object_or_404, redirect
from .models import Formula, Category
from .forms import FormulaForm, CategoryForm
from django.db.models import Q

def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        formulas = Formula.objects.filter(Q(text__icontains=search_query))
    else:
        formulas = Formula.objects.all()
    return render(request, 'formulas/home.html', {'formulas': formulas, 'search_query': search_query})

def create_formula(request):
    form = FormulaForm(request.POST, request.FILES)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            form = FormulaForm()
            return render(request, 'formulas/create_formula.html', {'form': form, 'success': 'Formula created successfully!'})
        else:
            return render(request, 'formulas/create_formula.html', {'form': form, 'error': 'Something went wrong!'})
    else:
        form = FormulaForm()
    return render(request, 'formulas/create_formula.html', {'form': form})

def edit_formula(request, slug):
    formula = get_object_or_404(Formula, slug=slug)

    if request.method == 'POST':
        form = FormulaForm(request.POST, request.FILES, instance=formula)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FormulaForm(instance=formula)
    return render(request, 'formulas/edit_formula.html', {'form': form, 'formula': formula})

def delete_formula(request, slug):
    formula = get_object_or_404(Formula, slug=slug)

    if request.method == 'POST':
        formula.delete()
        return redirect('home')
    return render(request, 'formulas/delete_formula.html', {'formula': formula})

def sort_formulas(request):
    sort_value = request.GET.get('sort_value')
    sort_by = request.GET.get('sort_by')

    formulas = []

    if sort_by == 'slug':
        if sort_value:
            formulas = Formula.objects.filter(slug__icontains=sort_value).order_by('slug', 'category')
        else:
            formulas = Formula.objects.all().order_by('slug', 'category')

    elif sort_by == 'category':
        if sort_value:
            formulas = Formula.objects.filter(category__name__icontains=sort_value).order_by('category__name', 'slug')
        else:
            formulas = Formula.objects.all().order_by('category__name', 'slug')
    return render(request, 'formulas/sort_formulas.html', {'formulas': formulas, 'sort_by': sort_by, 'sort_value': sort_value})

def create_category(request):
    form = CategoryForm()
    categories = Category.objects.all()
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            category_name = form.cleaned_data['name']

            if Category.objects.filter(name=category_name).exists():
                return render(request, 'formulas/create_category.html', {'form': form, 'categories': categories, 'error': 'Category already exists!'})
            else:
                form.save()
                form = CategoryForm()
                return render(request, 'formulas/create_category.html', {'form': form, 'categories': categories})
    else:
        form = CategoryForm()
    return render(request, 'formulas/create_category.html', {'form': form, 'categories': categories})

def edit_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('create_category')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'formulas/edit_category.html', {'form': form, 'category': category})

def delete_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    if request.method == 'POST':
        category.delete()
        return redirect('create_category')
    return render(request, 'formulas/delete_category.html', {'category': category})