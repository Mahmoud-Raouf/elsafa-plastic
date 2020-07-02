from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    
    # Start workers
    path('workers/' , views.workers_list , name= 'workers_list'),
    path('add_workers/' , views.add_workers , name= 'add_workers'),
    path('edit_workers/<int:pk>/' , views.edit_workers , name= 'edit_workers'),
    path('workers_delete/<int:pk>/' , views.workers_delete , name= 'workers_delete'),
    # end workers

    # Start servicing
    path('servicing/' , views.servicing_list, name= 'servicing_list'),
    path('add_servicing/' , views.add_servicing, name= 'add_servicing'),
    path('edit_servicing/<int:pk>/' , views.edit_servicing, name= 'edit_servicing'),
    path('servicing_delete/<int:pk>/' , views.servicing_delete, name= 'servicing_delete'),
    # end servicing

    # Start servicing
    path('amount_received/<int:pk>/' , views.Amount_Received_list, name= 'amount_received_list'),
    path('add_amount_received/' , views.add_amount_received, name= 'add_amount_received'),
    path('edit_amount_received/<int:pk>/' , views.edit_amount_received, name= 'edit_amount_received'),
    path('amount_received_delete/<int:pk>/' , views.Amount_Received_delete, name= 'amount_received_delete'),
    # end servicing

]