from django import forms
from django.forms import ModelForm
from .models import ShippingAddress

class Checkout(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['customer', 'order']