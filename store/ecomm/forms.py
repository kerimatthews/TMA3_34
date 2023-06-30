from django import forms
from django.forms import ModelForm
from .models import OrderItem, Computer


class CartForm(ModelForm):
    computer = forms.IntegerField()
    price=forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model= OrderItem
        fields = ['computer', 'price']