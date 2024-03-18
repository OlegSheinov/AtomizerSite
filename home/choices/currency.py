from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyChoices(models.IntegerChoices):
    RUBLE = 1, _('Ruble ₽')
    EURO = 2, _('Euro €')
    DOLLAR = 3, _('Dollar $')
