import graphene

from home.api.quaries import LanguageQuery, UserQuery
from home.api.quaries import SettingsQuery


class Query(
    graphene.ObjectType,
    SettingsQuery,
    LanguageQuery,
    UserQuery
):
    class Meta:
        description = "Main Query"


schema = graphene.Schema(query=Query)
