from django.shortcuts import render
from expenses.models import Workers
from selling.models import Customer
from products.models import Product, ProductMix
from django.db.models.aggregates import Sum
from selling.models import Salary



def dashboard(request):

    workers = Workers.objects.all().count()
    workers_sum = Workers.objects.all().aggregate(Sum('price'))['price__sum']
    customers = Customer.objects.all().count()
    productmix = ProductMix.objects.all().count()
    salary = Salary.objects.all().count()


    return render(request , 'dashboard.html' , {
        'workers' : workers ,
        'customers' : customers ,
        'productmix' : productmix,
        'workers_sum' : workers_sum,
        'salary' : salary,
    })
