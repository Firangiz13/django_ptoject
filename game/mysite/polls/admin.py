from django.contrib import admin
from .forms import  Checkout
from . import models
# Register your models here.
from .models import ShippingAddress, Customer


admin.site.register(models.Customer),
admin.site.register(models.Product),
admin.site.register(models.Detail),
admin.site.register(models.Order),
admin.site.register(models.OrderItem),
admin.site.register(models.ShippingAddress),




# class CheckoutAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'address', 'country']
#     form = Checkout
#     list_filter = ['customer']
#     search_fields = ['customer','address']
#     admin.site.register(ShippingAddress, CheckoutAdmin),
#     admin.site.register(Customer)