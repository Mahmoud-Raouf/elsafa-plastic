from django.shortcuts import render
from expenses.models import Workers
from selling.models import Customer
from products.models import ProductMix
from django.db.models.aggregates import Sum


def dashboard(request):
    workers = Workers.objects.all().count()
    workers_sum = Workers.objects.all().aggregate(Sum('price'))['price__sum']
    customers = Customer.objects.all().count()
    productmix = ProductMix.objects.all().count()
    
    return render(request , 'dashboard.html' , {
        'workers' : workers ,
        'customers' : customers ,
        'productmix' : productmix,
    })
