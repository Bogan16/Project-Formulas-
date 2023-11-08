from django import forms
from .models import Formula, Category

class FormulaForm(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['text', 'photo_formulas', 'slug', 'category']
        
    photo_formulas = forms.ImageField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
    name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete': 'name'}))

