from django import forms
from .models import Order


class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    address = forms.CharField(widget=forms.Textarea, required=True)
    payment_method = forms.ChoiceField(
        choices=[('cash', 'Наличные'), ('card', 'Банковская карта')],
        widget=forms.RadioSelect,
        required=True
    )
