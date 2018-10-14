from django.contrib import admin

from .models import Deliverer, DeliveryItem, Address

# Register your models here.

admin.site.register(Deliverer)
admin.site.register(DeliveryItem)
admin.site.register(Address)
