from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext

from .models import ShippingAddress, Customer, User
from django.http import Http404, HttpResponseRedirect
from django.forms import inlineformset_factory
from .forms import  Checkout
# from django.template import RequestContext, loader


def index(request):
    return render(request, 'form.html')


def product_list(request):
    try:
        prd_list = ShippingAddress.objects.all()
    except:
        raise Http404("Shipping address is not found")
    prd_data = {'students': prd_list}
    return render(request, 'hello.html', context=prd_data)


# def my_view(request):
#     if request.method == 'POST':
#         # check_form = Checkout(request.POST)
#         # created_user = check_form.save(commit=False)
#         formset = CheckoutSet(request.POST, instance=request.user)
#     # if not request.user.is_staff or not request.user.is_superuser:
#     #     raise Http404
#         # formset = CheckoutSet(request.POST or None, request.FILES or None)
#         if formset.is_valid():
#             # created_user.save()
#             formset.save()
#         return HttpResponseRedirect('checkout')
#     else:
#         formset = CheckoutSet(instance=request.user)
#         context = {formset: 'formset'}
#         return render(request.user, "checkout.html", context)
# def someview(request):
#     if request.method == 'post':
#         form = Checkout(request.POST, name=request.user)
#         if form.is_valid():
#             selected_name = form.cleaned_data.get('name')
#
#     else:
#         form = Checkout(name=request.user)
#
#     context = {form: 'form'}
#
#     return render(request, 'checkout.html', context,
#         context_instance=RequestContext(request))
# def someview(request):
#     if request.method == 'POST':
#         check_form = CheckoutForm(request.POST)
#         if check_form.is_valid():
#             check_form.cleaned_data.get('name')
#
#     else:
#         check_form =CheckoutForm
#
#     context = {'check_form': check_form, }
#     instance = RequestContext(request)
#
#     return render(request, 'checkout.html', context)


# def checkout(request):
#     if request.method == 'POST':
#         checkk_form = CustomerForm(request.POST)
#
#         if checkk_form.is_valid():
#
#
#             checkk_form.save()
#
#             return redirect('checkout')
#         else:
#             print(checkk_form.errors)
#     else:
#         checkk_form = CustomerForm()
#
#     context = {'checkk_form': checkk_form}

    # return render(request, 'checkout.html', context)



def checkout(request):
    if request.method == 'POST':
        check_form = Checkout(request.POST)

        if check_form.is_valid():


            check_form.save()

            return redirect('checkout.html')
        else:
            print(check_form.errors)

    else:
        check_form = Checkout()
    context = {'check_form': check_form}
    return render(request, 'checkout.html', context)


# def someview(request):
#     if request.method == 'post':
#         check_form = Checkout(request.POST, instance=request.user)
#         if check_form.is_valid():
#             selected_name = check_form.cleaned_data.get('name')
#             check_form.save()
#
#     else:
#         check_form = Checkout(instance=request.user)
#     context = {'check_form': check_form}
#
#     context_instance = RequestContext(request)
#     return render(request, 'checkout.html', context)
