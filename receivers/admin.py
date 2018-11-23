from django.contrib import admin

from .models import Receiver, ReceiverGroup, ReceiverCompany

# Register your models here.

admin.site.register(Receiver)
admin.site.register(ReceiverGroup)
admin.site.register(ReceiverCompany)

