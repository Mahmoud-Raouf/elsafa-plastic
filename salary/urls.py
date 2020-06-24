from django.urls import path
from . import views

app_name = 'salary'

urlpatterns = [
    
    # Start Salary
    path('salary/' , views.salary_list, name= 'salary_list'),
    path('add_salary/' , views.add_salary, name= 'add_salary'),
    path('edit_salary/<int:pk>/' , views.edit_salary, name= 'edit_salary'),
    path('salary_delete/<int:pk>/' , views.salary_delete, name= 'salary_delete'),
    # end Salary

    # Start Purchasing
    path('purchasing/' , views.purchasing_list, name= 'purchasing_list'),
    path('add_purchasing/' , views.add_purchasing, name= 'add_purchasing'),
    path('edit_purchasing/<int:pk>/' , views.edit_purchasing, name= 'edit_purchasing'),
    path('purchasing_delete/<int:pk>/' , views.purchasing_delete, name= 'purchasing_delete'),
    # end Purchasing

]