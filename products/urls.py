from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    # Start Product_Mix
    path('productmix/' , views.productmix_list, name= 'productmix_list'),
    path('add_productmix/' , views.add_productmix, name= 'add_productmix'),
    path('edit_productmix/<int:pk>/' , views.edit_productmix, name= 'edit_productmix'),
    path('productmix_delete/<int:pk>/' , views.productmix_delete, name= 'productmix_delete'),
    # end Product_Mix

    # # Start ProductMix_Detail
    # path('add_ProductMix_Detail/' , views.add_ProductMix_Detail, name= 'add_ProductMix_Detail'),
    # path('ProductMix_Detail_list/' , views.ProductMix_Detail_list, name= 'ProductMix_Detail_list'),
    # path('ProductMix_Detail_delete/<int:pk>/' , views.ProductMix_Detail_delete, name= 'ProductMix_Detail_delete'),
    # # end ProductMix_Detail

    # Start roll
    path('roll/' , views.roll_list, name= 'roll_list'),
    path('add_roll/' , views.add_roll, name= 'add_roll'),
    path('edit_roll/<int:pk>/' , views.edit_roll, name= 'edit_roll'),
    path('roll_delete/<int:pk>/' , views.roll_delete, name= 'roll_delete'),
    # end roll

    # Start Product
    path('product/' , views.product_list, name= 'product_list'),
    path('add_product/' , views.add_product, name= 'add_product'),
    path('edit_product/<int:pk>/' , views.edit_product, name= 'edit_product'),
    path('product_delete/<int:pk>/' , views.product_delete, name= 'product_delete'),
    # end Product
]