from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.fields import RichTextField

from home.choices.currency import CurrencyChoices


class Tariffs(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, unique=True, default=_("Tariff 1"),
                            verbose_name=_("Tariff Name"))
    description = RichTextField(blank=True, null=True, verbose_name=_("Tariff description"))
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, verbose_name=_("Tariff price"))
    currency = models.CharField(
            verbose_name=_("Purpose of the request"),
            choices=CurrencyChoices.choices,
            max_length=16
        )
    uses = models.IntegerField(verbose_name=_("Uses in the tariff"), default=0)
    end_date = models.DateField(verbose_name=_("End Date"), blank=True, null=True)
