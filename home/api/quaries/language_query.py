import graphene
from django.conf import settings
from graphene_django import DjangoObjectType


class LanguageNode(graphene.ObjectType):
    name = graphene.String()
    code = graphene.String()

    def resolve_code(self: tuple, info):
        return self[0]

    def resolve_name(self: tuple, info):
        return self[1]


class LanguageQuery:
    languages = graphene.List(LanguageNode)

    def resolve_languages(self, info, **kwargs):
        languages_list = settings.LANGUAGES
        return languages_list
