from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', include('products.urls' , namespace='products')),
    path('selling/', include('selling.urls' , namespace='selling')),
    path('expenses/', include('expenses.urls' , namespace='expenses')),
    path('orders/', include('orders.urls' , namespace='orders')),
    path('dashboard/', include('dashboard.urls' , namespace='dashboard')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)