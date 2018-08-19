from django.db.models.fields import CharField, BooleanField
from django.db.models import Model, ForeignKey, CASCADE
from django.utils.translation import gettext as _

# Create your models here.


class Workplace(Model):
    """
    Where Collectors work
    """
    workplace_name = CharField(max_length=120, blank=False, null=False)
    workplace_address = ForeignKey('deliverers.Address', on_delete=CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = _('Workplace')
        verbose_name_plural = _('Workplaces')


class ReceiverGroup(Model):
    receiver_group_name = CharField(_('Group Name'), max_length=50, null=False, blank=False)
    receiver_group_office = CharField(_('Office # and Floor #'), max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _('Receiver Group')
        verbose_name_plural = _('Receiver Groups')


class ReceiverGroupMember(Model):
    receiver = ForeignKey('receivers.Receiver', on_delete=CASCADE, blank=False, null=False)
    receiver_group = ForeignKey('ReceiverGroup', on_delete=CASCADE, blank=False, null=False)
    is_money_person = BooleanField(_('Is Collecting Money'), default=False, null=False, blank=False)
    is_money_person_deputy = BooleanField(_('Is Collecting Money (Deputy)'), default=False, null=False, blank=False)

    class Meta:
        verbose_name = _('Receiver Group Member')
        verbose_name_plural = _('Receiver Group Members')
