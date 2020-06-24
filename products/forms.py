from django import forms
from .models import ProductMix , Product , Roll
from django.forms import modelformset_factory

class ProductMixForm(forms.ModelForm):
    class Meta:
        model = ProductMix
        fields = ("name","image"
        ,"type1",'type1_count','type1_price','price1'
        ,"type2",'type2_count','type2_price','price2',
        "type3",'type3_count' ,'type3_price','price3'
        ,"type4",'type4_count','type4_price','price4',
        "type5",'type5_count','type5_price','price5',
        "description")
class RollForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = ("productmix","name","size","image","description"
        ,"cost","price",'roll_price',"profit")

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("roll","name","size","image" ,"description"
        ,"cost","price","profit")
