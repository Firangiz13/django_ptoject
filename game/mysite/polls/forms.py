

from django import forms
from .models import ShippingAddress


class Checkout(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['customer', 'order', ]










from django.forms import inlineformset_factory


# CheckoutSet = inlineformset_factory(Customer, ShippingAddress, fields=('zipcode',))
# customer = ShippingAddress.objects.get(customer_id='')
# formset = CheckoutSet(instance=customer)


# class CheckoutForm(forms.ModelForm):
#     class Meta:
#         model = ShippingAddress
#         fields = '__all__'
#         # exclude = ('customer',)

# class  CustomerForm(forms.ModelForm):
#
#      class Meta:
#          model = Customer
#          fields = ('name', 'email')
         # exclude = ('email',)

         # def __init__(self):
         #     self.name = User
         #
         # def __str__(self):
         #     return self.name

#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', '')
#         super(CheckoutForm, self).__init__(*args, **kwargs)
#         self.fields['name'] = forms.ModelChoiceField(queryset=Customer.objects.filter(name=user))
#         self.fields['email'] = forms.CharField(max_length=255)


class Checkout(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        exclude = ['customer', 'order',]

        # def __init__(self, *args, **kwargs):
        #     user = kwargs.pop('user', '')
        #     super(Checkout, self).__init__(*args, **kwargs)
        #     self.fields['name'] = forms.ModelChoiceField(queryset=Customer.objects.filter(name=user))


# CheckoutSet = inlineformset_factory(Customer, ShippingAddress, form=Checkout, extra=1)

# class Payment(forms.ModelForm):
#        class Meta:
#            model = ShippingAddress
#            fields = ('name', 'number', 'exp_month', 'exp_year')
# class Checkout(forms.ModelForm):
#     # transaction_id = forms.CharField(widget=forms.CharField)
#     class Meta:
#         model = Payment
#         fields = ('Exp_year', 'Exp_month')
# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = ShippingAddress
#         exclude = ('customer','order')

