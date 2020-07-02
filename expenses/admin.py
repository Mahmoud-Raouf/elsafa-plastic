from django.contrib import admin

from .models import Workers , Servicing , Amount_Received
admin.site.register(Workers)
admin.site.register(Servicing)
admin.site.register(Amount_Received)
