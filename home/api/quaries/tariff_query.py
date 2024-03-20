from datetime import datetime

import graphene
from graphene_django import DjangoObjectType
from wagtail.templatetags.wagtailcore_tags import richtext

from home.models import Tariffs
from home.utils.html import to_html


class TariffNode(DjangoObjectType):
    currency = graphene.String()

    class Meta:
        model = Tariffs
        only_fields = "__all__"

    def resolve_description(self: Tariffs, info):
        return to_html(richtext(self.description))

    def resolve_currency(self: Tariffs, info):
        return self.get_currency_display()


class TariffQuery:
    get_tariffs = graphene.List(TariffNode)

    def resolve_get_tariffs(self, info):
        return Tariffs.objects.filter(end_date__gte=datetime.now()).order_by("id")
