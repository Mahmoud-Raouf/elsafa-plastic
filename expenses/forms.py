from django import forms
from .models import Workers ,  Servicing

class WorkersForm(forms.ModelForm):
    
    class Meta:
        model = Workers
        fields = ("name","type_of_person","description",
        "price" , "amount_received", "remaining_amount")

class ServicingForm(forms.ModelForm):
    
    class Meta:
        model = Servicing
        fields = ("name","description","cost")
