from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    #    fields = [
    #        'name',
    #        'description',
    #        'quantity',
    #        'category',
    #        'price',
    #    ]

# ProductForm without Meta
class Example_ProductForm(forms.Form): 
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    quantity = forms.IntegerField(label='Quantity')
    category = forms.ModelChoiceField(
        label='Category', queryset=Category.objects.all(),
    )
    price = forms.FloatField(label='Price')