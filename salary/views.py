from django.shortcuts import get_object_or_404, redirect, render
from .models import Salary , Purchasing
from .forms import SalaryForm , PurchasingForm
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
            return redirect('salary:salary_list')
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
            return redirect('salary:salary_list')
    else:
        edit_salary_form = SalaryForm( instance=obj)
    return render(request ,'salary/edit_salary.html', {
        'edit_salary_form' : edit_salary_form ,
    })

def salary_delete(request , pk):
    salary_delete = Salary.objects.get(pk=pk).delete()
    return redirect('salary:salary_list')
# end Salary


# Start Purchasing
def purchasing_list(request):
    purchasing_list = Purchasing.objects.all()
    return render(request ,'purchasing/purchasing_list.html', {
    'purchasing_list': purchasing_list,
    })

def add_purchasing(request):
    purchasing_form = PurchasingForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        purchasing_form = PurchasingForm(request.POST or None , request.FILES)
        if purchasing_form.is_valid():
            purchasing_form.save()
            return redirect('salary:purchasing_list')
    else:
        purchasing_form = PurchasingForm()
    return render(request ,'purchasing/add_purchasing.html', {
        'purchasing_form' : purchasing_form ,
    })

def edit_purchasing(request , pk):
    obj = get_object_or_404(Purchasing , pk = pk)
    edit_purchasing_form = PurchasingForm(request.POST or None , request.FILES , instance=obj)
    if request.method == 'POST':
        edit_purchasing_form = PurchasingForm(request.POST or None , request.FILES, instance=obj)
        if edit_purchasing_form.is_valid():
            edit_purchasing_form.save()
            return redirect('salary:purchasing_list')
    else:
        edit_purchasing_form = PurchasingForm(instance=obj)
    return render(request ,'purchasing/edit_purchasing.html', {
        'edit_purchasing_form' : edit_purchasing_form,
    })

def purchasing_delete(request , pk):
    purchasing_delete = Purchasing.objects.get(pk=pk).delete()
    return redirect('salary:purchasing_list')

# end Purchasing