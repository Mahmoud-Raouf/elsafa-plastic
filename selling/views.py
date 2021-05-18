from django.shortcuts import get_object_or_404, redirect, render
from .models import Salary , Purchasing
from .forms import SalaryForm , PurchasingForm
from selling.models import Customer
from selling.forms import CustomerForm


# Start Salary
def salary_list(request):
    salary_list = Salary.objects.all()
    return render(request ,'salary/salary_list.html', {
        'salary_list' : salary_list ,
    })

def add_salary(request):
    salary_form = SalaryForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        salary_form = SalaryForm(request.POST or None , request.FILES)
        if salary_form.is_valid():
            salary_form.save()
            return redirect('selling:salary_list')
    else:
        salary_form = SalaryForm()
    return render(request ,'salary/add_salary.html', {
        'salary_form' : salary_form ,
    })

def edit_salary(request , pk):
    obj = get_object_or_404(Salary , pk = pk)
    edit_salary_form = SalaryForm(request.POST or None , request.FILES , instance=obj)
    if request.method == 'POST':
        edit_salary_form = SalaryForm(request.POST or None , request.FILES , instance=obj)
        if edit_salary_form.is_valid():
            edit_salary_form.save()
            return redirect('selling:salary_list')
    else:
        edit_salary_form = SalaryForm( instance=obj)
    return render(request ,'salary/edit_salary.html', {
        'edit_salary_form' : edit_salary_form ,
    })

def salary_delete(request , pk):
    salary_delete = Salary.objects.get(pk=pk).delete()
    return redirect('selling:salary_list')
# end Salary


# Start Purchasing
def purchasing_list(request):
    purchasing_list = Purchasing.objects.all()
    return render(request ,'purchasing/purchasing_list.html', {
    'purchasing_list': purchasing_list,
    })

def add_purchasing(request):
    customer_form = PurchasingForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        customer_form = PurchasingForm(request.POST or None , request.FILES)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('salary:purchasing_list')
    else:
        customer_form = PurchasingForm()
    return render(request ,'purchasing/add_purchasing.html', {
        'customer_form' : customer_form ,
    })

def edit_purchasing(request , pk):
    obj = get_object_or_404(Purchasing , pk = pk)
    edit_customer_form = PurchasingForm(request.POST or None , request.FILES , instance=obj)
    if request.method == 'POST':
        edit_customer_form = PurchasingForm(request.POST or None , request.FILES, instance=obj)
        if edit_customer_form.is_valid():
            edit_customer_form.save()
            return redirect('salary:purchasing_list')
    else:
        edit_customer_form = PurchasingForm(instance=obj)
    return render(request ,'purchasing/edit_purchasing.html', {
        'edit_customer_form' : edit_customer_form,
    })

def purchasing_delete(request , pk):
    purchasing_delete = Purchasing.objects.get(pk=pk).delete()
    return redirect('salary:purchasing_list')

# end Purchasing



# Start Customer
def customer_list(request):
    customer_list = Customer.objects.all()
    return render(request ,'customer/customer_list.html', {
    'customer_list': customer_list,
    })

def add_customer(request):
    customer_form = CustomerForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST or None , request.FILES)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('selling:customer_list')
    else:
        customer_form = CustomerForm()
    return render(request ,'customer/add_customer.html', {
        'customer_form' : customer_form ,
    })

def edit_customer(request , pk):
    obj = get_object_or_404(Customer , pk = pk)
    edit_customer_form = CustomerForm(request.POST or None , request.FILES , instance=obj)
    if request.method == 'POST':
        edit_customer_form = CustomerForm(request.POST or None , request.FILES, instance=obj)
        if edit_customer_form.is_valid():
            edit_customer_form.save()
            return redirect('selling:customer_list')
    else:
        edit_customer_form = CustomerForm(instance=obj)
    return render(request ,'customer/edit_customer.html', {
        'edit_customer_form' : edit_customer_form,
    })

def customer_delete(request , pk):
    customer_delete = Customer.objects.get(pk=pk).delete()
    return redirect('selling:customer_list')

# end Customer