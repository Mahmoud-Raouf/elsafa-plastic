from django.shortcuts import get_object_or_404, redirect, render
from .models import Servicing , Workers
from .forms import WorkersForm ,ServicingForm
from expenses.models import Amount_Received
from expenses.forms import Amount_ReceivedForm

# Start Workers
def workers_list(request):
    # workers = Amount_Received.objects.all()
    workers = Workers.objects.all()
    return render(request ,'workers/workers_list.html', {
        'workers' : workers ,
        'title' : 'قائمة الموظفون'
    })


def add_workers(request):
    workers_form = WorkersForm(request.POST)
    if request.method == 'POST':
        workers_form = WorkersForm(request.POST)
        if workers_form.is_valid():
            workers_form.save()
            return redirect('expenses:workers_list')
    else:
        workers_form = WorkersForm()
    return render(request ,'workers/add_workers.html', {
        'workers_form' : workers_form,
    })


def edit_workers(request , pk):
    obj = get_object_or_404(Workers , pk=pk)
    workers_form = WorkersForm(request.POST or None , instance=obj)
    if request.method == 'POST':
        workers_form = WorkersForm(request.POST or None , instance=obj)
        if workers_form.is_valid():
            workers_form.save()
            return redirect('expenses:workers_list')
    else:
        workers_form = WorkersForm(instance=obj)
    return render(request ,'workers/edit_workers.html', {
        'workers_form' : workers_form,
    })


def workers_delete(request, pk):
    workers_delete = Workers.object.get(pk=pk)
    workers_delete.delete()
    return redirect('expenses:workers_list')
# end Workers


# Start Amount_Received
def Amount_Received_list(request, pk):
    amount_received = Amount_Received.objects.filter(workers = pk)
    return render(request ,'amount_received/Amount_Received_list.html', {
        'amount_received' : amount_received ,
        'title' : 'قائمة الموظفون'
    })

def add_amount_received(request):
    amount_received_form = Amount_ReceivedForm(request.POST)
    if request.method == 'POST':
        amount_received_form = Amount_ReceivedForm(request.POST)
        if amount_received_form.is_valid():
            amount_received_form.save()
            return redirect('expenses:workers_list')
    else:
        amount_received_form = Amount_ReceivedForm()
    return render(request ,'amount_received/add_amount_received.html', {
        'amount_received_form' : amount_received_form,
    })

def edit_amount_received(request , pk):
    obj = get_object_or_404(Amount_Received , pk=pk)
    edit_amount_received_form = Amount_ReceivedForm(request.POST or None , instance=obj)
    if request.method == 'POST':
        edit_amount_received_form = Amount_ReceivedForm(request.POST or None , instance=obj)
        if edit_amount_received_form.is_valid():
            edit_amount_received_form.save()
            return redirect('expenses:workers_list')
    else:
        edit_amount_received_form = Amount_ReceivedForm(instance=obj)
    return render(request ,'amount_received/edit_amount_received.html', {
        'edit_amount_received_form' : edit_amount_received_form,
    })


def Amount_Received_delete(request, pk):
    workers_delete = Amount_Received.objects.get(pk=pk)
    workers_delete.delete()
    return redirect('expenses:workers_list')
# end Amount_Received


# Start Servicing
def servicing_list(request):
    servicing_list = Servicing.objects.all()
    return render(request ,'servicing/servicing_list.html', {
        'servicing_list' : servicing_list,
    })


def add_servicing(request):
    servicing_form = ServicingForm(request.POST)
    if request.method == 'POST':
        workers_form = ServicingForm(request.POST)
        if workers_form.is_valid():
            workers_form.save()
            return redirect('expenses:servicing_list')
    else:
        workers_form = ServicingForm()
    return render(request ,'servicing/add_servicing.html', {
        'servicing_form' : servicing_form ,
    })


def edit_servicing(request , pk):
    obj = get_object_or_404(Servicing , pk=pk)
    servicing_form = ServicingForm(request.POST or None , instance=obj)
    if request.method == 'POST':
        workers_form = ServicingForm(request.POST or None , instance=obj)
        if workers_form.is_valid():
            workers_form.save()
            return redirect('expenses:servicing_list')
    else:
        workers_form = ServicingForm(instance=obj)
    return render(request ,'servicing/edit_servicing.html', {
        'servicing_form' : servicing_form ,
    })


def servicing_delete(request , pk):
    servicing_delete = Servicing.objects.get(pk = pk)
    servicing_delete.delete()
    return redirect('expenses:servicing_list')
# end Servicing