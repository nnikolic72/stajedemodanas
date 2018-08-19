from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models import Model, ForeignKey, CASCADE
from django.utils.translation import gettext as _

# Create your models here.


class Receiver(Model):
    """
    Model for people who collect deliveries
    """
    user = ForeignKey(User, on_delete=CASCADE, blank=False, null=False)
    collector_first_name = CharField(_('First Name'), max_length=20, blank=False, null=False)
    collector_last_name = CharField(_('Last Name'), max_length=20, blank=True, null=True)
    collector_nickname = CharField(_('Nickname'), max_length=20, blank=True, null=True)
    phone_number = CharField(_('Phone Number'), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _('Receiver')
        verbose_name_plural = _('Receivers')
