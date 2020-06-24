from django.shortcuts import get_object_or_404, redirect, render
from .models import Product , ProductMix , Roll
from .forms import ProductMixForm , RollForm ,ProductForm
from django.db.models import Sum
from django.db.models import Avg, Count
from django.db.models.functions import Round

# Start Product_Mix
def productmix_list(request):
    product_mix  = ProductMix.objects.all()

    # for x in product_mix:
    #     productx = x.type1.price +  x.type2.price +  x.type3.price 

    return render(request ,'productsmix/productmix_list.html', {
        'product_mix' : product_mix ,
        # 'productx' : productx ,
        'title' : 'قائمة الخلطات',

    })

def add_productmix(request):
    # product_mix  = ProductMix_Detail.objects.all()
    productmix_form = ProductMixForm(request.POST , request.FILES)
    if request.method == 'POST':
        productmix_form = ProductMixForm(request.POST or None , request.FILES)
        if productmix_form.is_valid():
            # new_productmix = productmix_form.save(commit=False)
            # new_productmix.type1.price * new_productmix.type1_count
            # productx = x.type1.price +  x.type2.price +  x.type3.price +  x.type4.price +  x.type5.price 
            # new_productmix.price = productx
            productmix_form.save()

            return redirect('products:productmix_list')
    else:
        productmix_form = ProductMixForm()
    return render(request ,'productsmix/add_productmix.html', {
        'productmix_form' : productmix_form ,
        'title' : 'إضافة خلطة',

    })


def edit_productmix(request, pk):
    product_mix  = ProductMix.objects.all()
    obj = get_object_or_404(ProductMix , pk=pk)
    productmix_form = ProductMixForm(request.POST , request.FILES , instance=obj)
    if request.method == 'POST':
        productmix_form = ProductMixForm(request.POST or None , request.FILES , instance=obj)
        if productmix_form.is_valid():
            productmix_form.save()
            return redirect('products:productmix_list')
    else:
        productmix_form = ProductMixForm(  instance=obj)
    return render(request ,'productsmix/edit_productmix.html', {
        'productmix_form' : productmix_form,
        'title' : 'تعديل خلطة',

    })

def productmix_delete(request , pk):
    productmix_delete = ProductMix.objects.get(pk=pk)
    productmix_delete.delete()
    return redirect('products:productmix_list')
# end Product_Mix


# # Start ProductMix_Detail
# def add_ProductMix_Detail(request):
#     add_ProductMix_Detail = ProductMix_DetailForm(request.POST)
#     if request.method == 'POST':
#         add_ProductMix_Detail = ProductMix_DetailForm(request.POST or None)
#         if add_ProductMix_Detail.is_valid():
#             add_ProductMix_Detail.save()
#             return redirect('products:ProductMix_Detail_list')
#     else:
#         add_ProductMix_Detail = ProductMix_DetailForm()
#     return render(request ,'ProductMix_Detail/add_ProductMix_Detail.html', {
#         'add_ProductMix_Detail' : add_ProductMix_Detail ,
#         'title' : 'إضافة خلطة',

#     })

# def ProductMix_Detail_list(request):
#     ProductMix_Detail_list = ProductMix_Detail.objects.all()

#     if request.method == 'POST':
#         add_ProductMix_Detail = get_object_or_404(ProductMix_Detail , id=request.POST.get('ProductMix'))
#         new_price = request.POST.get('new_price')
#         add_ProductMix_Detail.price = int(new_price)
#         add_ProductMix_Detail.save()
#         return redirect('products:ProductMix_Detail_list')
#     else:
#         add_ProductMix_Detail = ProductMix_DetailForm()
#     return render(request ,'ProductMix_Detail/ProductMix_Detail_list.html', {
#         'ProductMix_Detail_list' : ProductMix_Detail_list ,
#         'title' : 'إضافة خلطة',

#     })

# def ProductMix_Detail_delete(request , pk):
#     ProductMix_Detail_delete = ProductMix_Detail.objects.get(pk=pk)
#     ProductMix_Detail_delete.delete()
#     return redirect('products:ProductMix_Detail_list')

# # Start ProductMix_Detail



# Start Roll
def roll_list(request):
    roll_list = Roll.objects.all()

        
    return render(request ,'roll/roll_list.html', {
        'roll_list' : roll_list ,
        'title' : 'قائمة الرولات',

    })

def add_roll(request):
    roll_form = RollForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        roll_form = RollForm(request.POST or None , request.FILES)
        if roll_form.is_valid():
            new_roll = roll_form.save(commit=False)
            new_roll.profit = new_roll.price - new_roll.cost.price  *  new_roll.size
            new_roll.roll_price =  new_roll.price  *  new_roll.size
            new_roll.save()
            return redirect('products:roll_list')
    else:
        roll_form = RollForm()
    return render(request ,'roll/add_roll.html', {
        'roll_form' : roll_form ,
        'title' : 'إضافة رول'  ,
    })

def edit_roll(request , pk):
    obj = get_object_or_404(Roll ,pk = pk)
    edit_roll_form = RollForm(request.POST or None , request.FILES , instance=obj)
    if request.method == 'POST':
        edit_roll_form = RollForm(request.POST or None , request.FILES, instance=obj)
        if edit_roll_form.is_valid():
            edit_roll_form.save()
            return redirect('products:roll_list')
    else:
        edit_roll_form = RollForm( instance=obj)
    return render(request ,'roll/edit_roll.html', {
        'edit_roll_form' : edit_roll_form,
        'title' : 'تعديل رول',
    })

def roll_delete(request, pk):
    roll_delete = Roll.objects.get(pk=pk)
    roll_delete.delete()
    return redirect('products:roll_list')
# end Roll


# Start Product
def product_list(request):
    products = Product.objects.all()
    return render(request ,'products/product_list.html', {
        'products' : products ,
        'title' : 'قائمة المنتجات ',

    })

def add_product(request):
    product_form = ProductForm(request.POST or None , request.FILES)
    if request.method == 'POST':
        product_form = ProductForm(request.POST or None , request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect('products:product_list')
    else:
        product_form = ProductForm()
    return render(request ,'products/add_product.html', {
        'product_form' : product_form ,
        'title' : 'إضافة منتج',

    })

def edit_product(request, pk):
    obj = get_object_or_404(Product , pk=pk)
    edit_product_form = ProductForm(request.POST or None , request.FILES , instance=obj)
    if request.method == 'POST':
        edit_product_form = ProductForm(request.POST or None , request.FILES , instance=obj)
        if edit_product_form.is_valid():
            edit_product_form.save()
            return redirect('products:product_list')
    else:
        edit_product_form = ProductForm(instance=obj)
    return render(request ,'products/edit_product.html', {
        'edit_product_form' : edit_product_form ,
        'title' : 'تعديل منتج',

    })

def product_delete(request , pk):
    product_delete = Product.objects.get(pk=pk).delete()
    return redirect('products:product_list')
# end Product