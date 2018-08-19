
from django_countries.fields import CountryField

from django.db.models.fields import CharField, DecimalField, BooleanField
from django.db.models import Model, ForeignKey, CASCADE
from django.utils.translation import gettext as _


class Deliverer(Model):
    """
    Model for companies/people that deliver
    """
    deliverer_name = CharField(max_length=100, blank=False, null=False)
    deliverer_phone = CharField(max_length=20, blank=False, null=False)


class Collector(Model):
    """
    Model for people who collect deliveries
    """
    user = ForeignKey('User', on_delete=CASCADE, blank=False, null=False)
    collector_first_name = CharField(_('First Name'), max_length=20, blank=False, null=False)
    collector_last_name = CharField(_('Last Name'), max_length=20, blank=True, null=True)
    collector_nickname = CharField(_('Nickname'), max_length=20, blank=True, null=True)
    phone_number = CharField(_('Phone Number'), blank=True, null=True)

    class Meta:
        verbose_name = _('Collector')
        verbose_name_plural = _('Collectors')


class DeliveryItem(Model):
    item_name = CharField(_('Item Name'), max_length=120, blank=False, null=False)
    item_description = CharField(_('Item Description'), max_length=1024, blank=True, null=True)
    item_price = DecimalField(_('Item Price'), max_digits=16, decimal_places=2, blank=False, null=False)
    item_deliverer_code = CharField(_('Item Code'), max_length=100, blank=True, null=True)
    deliverer = ForeignKey('Deliverer', on_delete=CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = _('Delivery Item')
        verbose_name_plural = _('Delivery Items')


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


class Workplace(Model):
    """
    Where Collectors work
    """
    workplace_name = CharField(max_length=120, blank=False, null=False)
    workplace_address = ForeignKey('Address', on_delete=CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = _('Workplace')
        verbose_name_plural = _('Workplaces')


class CollectorGroup(Model):
    collector_group_name = CharField(_('Group Name'), null=False, blank=False)
    collector_group_office = CharField(_('Office # or Floor #'), null=True, blank=True)


class CollectorGroupMember(Model):
    collector = ForeignKey('Collector', on_delete=CASCADE, blank=False, null=False)
    collector_group = ForeignKey('CollectorGroup', on_delete=CASCADE, blank=False, null=False)
    is_money_person = BooleanField(_('Is Collecting Money'), default=False, null=False, blank=False)
    is_money_person_deputy = BooleanField(_('Is Collecting Money (Deputy)'), default=False, null=False, blank=False)

