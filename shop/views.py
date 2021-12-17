from django.shortcuts import render
from .models import *
from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.http import Http404, HttpResponseRedirect
from django.forms import inlineformset_factory
from .forms import  Checkout


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html', context)

def men(request):
    products = Product.objects.filter(category='men')

    #for search bar

    product_name = request.GET.get('product_name')

    if product_name != '' and product_name is not None:
        products = products.filter(title__icontains=product_name)
    
    context = {'products': products}
    return render(request, 'shop/men.html', context)

def women(request):
    products = Product.objects.filter(category='women')

    #for search bar

    product_name = request.GET.get('product_name')
    
    if product_name != '' and product_name is not None:
        products = products.filter(title__icontains=product_name)
    context = {'products': products}

    return render(request, 'shop/women.html', context)

def kids(request):
    products = Product.objects.filter(category='kids')

    #for search bar

    product_name = request.GET.get('product_name')
    
    if product_name != '' and product_name is not None:
        products = products.filter(title__icontains=product_name)

    context = {'products': products}
    return render(request, 'shop/kids.html', context)

def details(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'shop/details.html', context)

def cart(request):
    orderitem = OrderItem.objects.all()

    #total amount for both authenticated and not authenticated users:

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items': items, 'order': order, 'orderitems': orderitem}
    return render(request, 'shop/cart.html', context)

def checkout(request):
    data = ShippingAddress.objects.all()

    if request.method == 'POST':
        check_form = checkout(request.POST)
        if check_form.is_valid():
            check_form.save()
            return redirect('checkout.html')
        else:
            print(check_form.errors)
    else:
        check_form = Checkout()
    
    #total amount for both authenticated and not authenticated users:

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
     
   
    context = {'items': items, 'order': order, 'check_form': check_form}
    return render(request, 'shop/checkout.html', context)