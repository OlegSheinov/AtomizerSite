from django.db import models
from django.utils.translation import gettext_lazy as _


class CurrencyChoices(models.IntegerChoices):
    RUBLE = 1, _('RUB')
    EURO = 2, _('EUR')
    DOLLAR = 3, _('USD')
