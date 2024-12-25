from django import forms
from .models import Product, Category
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'name',
            'description',
            'category',
            'price',
            'quantity',
        ]

    def clean(self) -> dict[str, any]:
        cleaned_data = super().clean()
        description = cleaned_data.get('description')
        # if description is not None and len(description) < 20:
        #     raise ValidationError({
        #         'description': 'The description cannot be less than 20 characters long.',
        #     })

        name = cleaned_data.get("name")
        if name == description:
            raise ValidationError(
                "The description should not be identical to the name."
            )
        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы."
            )
        return name

# ProductForm without Meta
class Example_ProductForm(forms.Form): 
    name = forms.CharField(label='Name')
    description = forms.CharField(label='Description')
    quantity = forms.IntegerField(label='Quantity')
    category = forms.ModelChoiceField(
        label='Category', queryset=Category.objects.all(),
    )
    price = forms.FloatField(label='Price')