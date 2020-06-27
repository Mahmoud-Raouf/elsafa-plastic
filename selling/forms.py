from django import forms
from .models import Salary ,Purchasing , Customer

class SalaryForm(forms.ModelForm):
    
    class Meta:
        model = Salary
        fields = ("name" , "typeofproducts" , "description" , "price" , "count" , "profit")

class PurchasingForm(forms.ModelForm):
    
    class Meta:
        model = Purchasing
        fields = ("name"  , "description" , "price" , "count" , 'profit')


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ("name"  ,'phone1','phone2','phone3', "description" , "address" ,'old_profit', 'profit')
