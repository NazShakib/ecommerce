from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display=('name','email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','digital')

class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','date_created','transaction_id')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product','order','quantity','date_added')

class ShippingAdressAdmin(admin.ModelAdmin):
    list_display= ('customer','order','addess','city','state','zipcode','date_added')


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)
