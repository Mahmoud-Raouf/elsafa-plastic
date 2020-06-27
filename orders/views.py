from django.shortcuts import render


app_name = 'orders'
def orders(request):
    return render(request , 'orders.html' , {})
