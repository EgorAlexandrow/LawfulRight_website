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
            'name': 'Имя',
            'phone': 'Телефон',
            'email': 'Email',
            'problem': 'Опишите проблему',
            'confidential': 'Политикой конфиденциальности',
        }


    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
