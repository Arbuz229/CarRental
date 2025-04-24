from .models import Car
from django.forms import ModelForm, TextInput, CheckboxInput, FileInput, Textarea


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'is_available', 'photo', 'phone_number', 'description']

        widgets = {
            'name': TextInput(attrs={
                'placeholder': "Название автомобиля",
                'class': 'form-input'
            }),
            'is_available': CheckboxInput(attrs={
                'class': 'form-checkbox',
            }),
            'photo': FileInput(attrs={
                'class': 'form-input'
            }),
            'phone_number': TextInput(attrs={
                'placeholder': "Введите номер для связи",
                'class': 'form-input'
            }),
            'description': Textarea(attrs={
                'placeholder': "Дополнительная информация (необязательно)",
                'class': 'form-input',
                'rows': 4,
            }),
        }
