from . models import Bakery, BakeryСonsist
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, FileInput

class BakeryForms(ModelForm):
    class Meta:
        model=Bakery
        fields=['name', 'category', 'text','weight','price', 'image']

        widgets = {
            "name": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название выпечки'
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Тип выпечки'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Состав выпечки'
            }),
            "weight": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вес выпечки'
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена выпечки'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
            }),
        }

class OrderForms(ModelForm):
    class Meta:
        model=BakeryСonsist
        fields=['customer', 'phone', 'name','basis','cream', 'filling','price']

        widgets = {
            "customer": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Имя покупателя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон покупателя'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Выбранная выпечка'
            }),
            "basis": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Основа выпечки'
            }),

            "cream": Select(attrs={
                'class': 'form-control',
            }),
            "filling": Select(attrs={
                'class': 'form-control',
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена выпечки в целом'
            }),
        }