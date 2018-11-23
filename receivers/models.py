from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
from django.db.models import Model, ForeignKey, CASCADE, EmailField
from django.utils.translation import gettext as _


class Receiver(Model):
    """
    Model for people who collect deliveries
    """
    user = ForeignKey(get_user_model(), on_delete=CASCADE, blank=True, null=True)
    group = ForeignKey('ReceiverGroup', on_delete=CASCADE, blank=True, null=True)
    company = ForeignKey('ReceiverCompany', on_delete=CASCADE, blank=True, null=True)
    email = EmailField(_('Email Address'), blank=True, null=True)
    first_name = CharField(_('First Name'), max_length=20, blank=False, null=False)
    last_name = CharField(_('Last Name'), max_length=20, blank=True, null=True)
    nickname = CharField(_('Nickname'), max_length=20, blank=True, null=True)
    phone_number = CharField(_('Phone Number'), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _('Receiver')
        verbose_name_plural = _('Receivers')

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ReceiverGroup(Model):
    """
    Model for groups of receivers
    """
    name = CharField(_('Group Name'), max_length=100, blank=False, null=False)
    company = ForeignKey('ReceiverCompany', on_delete=CASCADE, blank=True, null=True)
    cashier = ForeignKey('Receiver', on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('Receiver Group')
        verbose_name_plural = _('Receiver Groups')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class ReceiverCompany(Model):
    """
    Where receivers work
    """
    name = CharField(_('Company Name'), max_length=100, blank=False, null=False)
    address = ForeignKey('deliverers.Address', on_delete=CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('Receiver Company')
        verbose_name_plural = _('Receiver Companies')

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
