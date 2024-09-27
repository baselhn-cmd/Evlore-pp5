from django import forms
from .models import Product
from .models import Review

class ProductForm(forms.ModelForm):
    """
    Show all fields from product model,
    so the staff can add products
    """
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'content')