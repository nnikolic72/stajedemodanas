from django.db.models import Model, ForeignKey, CASCADE, DecimalField, CharField
from django.db.models.fields import DateTimeField

# Create your models here.


class Order(Model):
    order_date = DateTimeField(null=True, blank=True)


class OrderLine(Model):
    item = ForeignKey('deliverers.DeliveryItem', null=True, blank=True, on_delete=CASCADE)
    order = ForeignKey('Order', null=False, blank=False, on_delete=CASCADE)
    receiver = ForeignKey('receivers.Receiver', null=True, blank=True, on_delete=CASCADE)
    quantity = DecimalField(null=True, blank=True, max_digits=16, decimal_places=2, default=1)
    notes = CharField(max_length=200, null=True, blank=True)
