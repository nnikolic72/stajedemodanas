from django_countries.fields import CountryField

from django.db.models.fields import CharField, DecimalField
from django.db.models import Model, ForeignKey, CASCADE
from django.utils.translation import gettext as _

# Create your models here.


class Deliverer(Model):
    """
    Model for companies/people that deliver
    """
    name = CharField(max_length=100, blank=False, null=False)
    phone = CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = _('Deliverer')
        verbose_name_plural = _('Deliverers')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class DeliveryItem(Model):
    name = CharField(_('Item Name'), max_length=120, blank=False, null=False)
    description = CharField(_('Item Description'), max_length=1024, blank=True, null=True)
    price = DecimalField(_('Item Price'), max_digits=16, decimal_places=2, blank=False, null=False)
    deliverer_code = CharField(_('Item Code'), max_length=100, blank=True, null=True)
    deliverer = ForeignKey('Deliverer', on_delete=CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = _('Delivery Item')
        verbose_name_plural = _('Delivery Items')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class Address(Model):
    """
    Class for storing Deliverers and Workplace addresses
    """
    address1 = CharField(_('Address line 1'), max_length=1024, blank=False, null=False)
    address2 = CharField(_('Address line 2'), max_length=1024, blank=True, null=True)
    zip_code = CharField(_('ZIP / Postal code'), max_length=12, blank=True, null=True)
    city = CharField(_('City'), max_length=1024, blank=True, null=True)
    country = CountryField(_('Country'), blank=True, null=True)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __repr__(self):
        return f'{self.address1}, {self.city}'

    def __str__(self):
        return f'{self.address1}, {self.zip_code}, {self.city}, {self.country}'
