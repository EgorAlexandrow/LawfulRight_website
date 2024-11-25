from django import forms
from homepage.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'email', 'problem', 'confidential']
        widgets = {
            'problem': forms.Textarea(attrs={'rows': 7}),
        }
        labels = {
            'name': 'Имя:',
            'phone': 'Телефон:',
            'email': 'Email:',
            'problem': 'Опишите проблему',
            'confidential': 'Политикой конфиденциальности',
        }
