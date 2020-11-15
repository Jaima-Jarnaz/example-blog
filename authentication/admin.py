from django.contrib import admin
from .models import Customer
class AdminCustomer(admin.ModelAdmin):
    list_display=['firstname','lastname','email','password','confirmpassword']   




# Register your models here.
admin.site.register(Customer,AdminCustomer)
