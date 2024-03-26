from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    tg_id = models.IntegerField(unique=True, verbose_name=_("Telegram ID"), null=True, blank=True)
    tg_username = models.CharField(max_length=64, null=True,  verbose_name=_("Telegram Username"))
    tg_first_name = models.CharField(max_length=64, null=True,  verbose_name=_("Telegram first name"))
    tg_last_name = models.CharField(max_length=64, null=True,  verbose_name=_("Telegram last name"))
    tariff = models.ForeignKey(
        "home.Tariffs", verbose_name=_("Tariff"), on_delete=models.SET_NULL, null=True
    )
    total_uses = models.PositiveIntegerField(default=0, verbose_name=_("Total uses"))
    uses_left = models.PositiveIntegerField(default=0, verbose_name=_("Uses left"))
    lang = models.CharField(max_length=4, default='en')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('Users')
