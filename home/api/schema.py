import graphene

from home.api.quaries import LanguageQuery
from home.api.quaries import SettingsQuery


class Query(
    graphene.ObjectType,
    SettingsQuery,
    LanguageQuery
):
    class Meta:
        description = "Main Query"


schema = graphene.Schema(query=Query)
