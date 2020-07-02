from django import forms
from .models import Workers ,  Servicing , Amount_Received

class Amount_ReceivedForm(forms.ModelForm):
    
    class Meta:
        model = Amount_Received
        fields = ('workers' , 'amount_received' , 'description' )
        
class WorkersForm(forms.ModelForm):
    
    class Meta:
        model = Workers
        fields = ("name","type_of_person","description",
        "price" )

class ServicingForm(forms.ModelForm):
    
    class Meta:
        model = Servicing
        fields = ("name","description","cost")
