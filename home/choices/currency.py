from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyChoices(models.TextChoices):
    RUBLE = 'RUBLE', _('Ruble ₽')
    EURO = 'EURO', _('Euro €')
    DOLLAR = 'DOLLAR', _('Dollar $')
