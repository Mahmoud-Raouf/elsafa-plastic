from django import forms
from salary.models import Salary ,Purchasing

class SalaryForm(forms.ModelForm):
    
    class Meta:
        model = Salary
        fields = ("name" , "typeofproducts" , "description" , "price" , "count" , "profit")

class PurchasingForm(forms.ModelForm):
    
    class Meta:
        model = Purchasing
        fields = ("name" , "typeofproduct" , "description" , "price" , "count" , 'profit')
