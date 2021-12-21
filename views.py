from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *


def home(request):
    products =Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/home.html',context)

def men(request, title__icontains=None):
    products = Product.object.filter(category='men')



    product_name = request.GET.get('product_name')

    if product_name != '' and product_name is not None:
        products = products.filter(title__icontains=product_name)

        context = {'products': products}
        return render(request, 'shop/men.html', context)

    def women(request):
        products = Product.objects.filter(category='women')



        product_name = request.GET.get('product_name')

        if product_name != '' and product_name is not None:
            products = products.filter(title__icontains=product_name)
        context = {'products': products}

        return render(request, 'shop/women.html', context)

    def kids(request):
        products = Product.objects.filter(category='kids')



        product_name = request.GET.get('product_name')

        if product_name != '' and product_name is not None:
             products = products.filter(title__icontains=product_name)

        context = {'products': products}
        return render(request, 'shop/kids.html', context)

    def details(request, id):
        product = Product.objects.get(id=id):
        size_and_color=Detail.objects.get(id=id)
        context = {'product': product, 'size_and_color': size_and_color}
        return render(request, 'shop/details.html', context)

    def cart(request):
        orderitem = OrderItem.objects.all()



        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = orderitem_set.all()
        else:
            items =[]
            order = {'get_cart_total':0, 'get_cart_items':0}

        context = {'items': items, 'order': order, 'orderitems': orderitem}
        return render(request, 'shop/cart.html', context)

    def checkout(request):
        data = ShippingAddress.objects.all()

        from = ShippingForm()
        if request.method == 'POST':
            form = ShippingForm(request.POST)
            if form.is_valid():
                form.save()



        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = Order.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total':0, 'get_cart_items':0}


        context = {'items': items, 'order': order, 'form':form}
        return render(request, 'shop/checkout.html', context)





































































