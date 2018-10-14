from django.contrib import admin

from .models import Workplace, ReceiverGroup, ReceiverGroupMember

# Register your models here.

admin.site.register(Workplace)
admin.site.register(ReceiverGroup)
admin.site.register(ReceiverGroupMember)
