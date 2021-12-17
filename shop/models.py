from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# Create your models here.

class Customer(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price=models.FloatField(default=0)
    category = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.title

class Detail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=100)
    image = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.product.title

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    card_name = models.CharField(max_length=200, null=True)
    number = models.IntegerField(null=True, blank=True)
    expmonth = models.IntegerField(null=True, blank=True)
    expyear = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.address



