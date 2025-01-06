import time

from django import forms
from homepage.models import Order


class OrderForm(forms.ModelForm):
    timestamp = forms.CharField(widget=forms.HiddenInput())


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
    

    def clean_timestamp(self):
        """Проверка времени отправки формы."""
        timestamp = self.cleaned_data.get('timestamp')
        if not timestamp:
            raise forms.ValidationError("Ошибка времени отправки формы.")

        try:
            timestamp = float(timestamp)
        except (TypeError, ValueError):
            raise forms.ValidationError("Некорректное значение времени.")

        current_time = time.time()
        if current_time - timestamp < 10:
            raise forms.ValidationError("Слишком быстро! Заполните форму внимательнее.")
        return timestamp
