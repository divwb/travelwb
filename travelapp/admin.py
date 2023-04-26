from django.contrib import admin

from .models import Places, Customer, Booking


# Register your models here.

@admin.register(Places)
class PlacesModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','offerprice','place','image']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
        list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']



@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','Address','dateofbirth','Requirements']
