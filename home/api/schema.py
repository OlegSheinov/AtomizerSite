import graphene

from home.api.quaries import LanguageQuery, UserQuery
from home.api.quaries import SettingsQuery
from home.api.quaries.tariff_query import TariffQuery


class Query(
    graphene.ObjectType,
    SettingsQuery,
    LanguageQuery,
    UserQuery,
    TariffQuery
):
    class Meta:
        description = "Main Query"


schema = graphene.Schema(query=Query)
