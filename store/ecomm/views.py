from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Computer, OrderItem, Order
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.http import Http404, HttpResponse
from decimal import *
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CartForm



#@login_required
# create a function
def ecomm(request):
    data = Computer.objects.all()
    context ={
        "data":data
    }
    # return response with template and context
    return render(request, "main.html", context)

def delete(request, item_id):
 #   comps=Computer.objects.get(pk=item_id)
    item=OrderItem.objects.get(computer=item_id)
    item.delete()
    return redirect('/cart/')


def computers(request):
    list = Computer.objects.all()
    context = {'list':list}
    return render(request, 'list.html', context)


def laptops(request):
    laptop = Computer.objects.filter(category="Laptop")
    context = {'laptop':laptop}
    return render(request, 'laptops.html', context)

def desktops(request):
    desktop = Computer.objects.filter(category="Desktop")
    context = {'desktop':desktop}
    return render(request, 'desktops.html', context)

@login_required
def cart(request):

    orderI=OrderItem.objects.all()
    output=[]
    comp=[]
    total=Decimal(0)
    for x in orderI:
        name_id=x.computer
        name= Computer.objects.get(id=name_id)
        output.append(name.price)
        total+=name.price
        comp.append(name)

    context = {'output':output,
               'comp': comp,
               'total':total}
    return render(request, 'cart.html', context)



class ComputerDetailView(DetailView):
    # specify the model to use
    model = Computer

class CartListView(ListView):
    # specify the model to use
    model = OrderItem




    
def add_to_cart(request):
    if request.POST:
        form=CartForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
         form.save()

        return redirect('/cart/')

    return render(request, 'add_to_cart.html', {'form':CartForm})