import graphene
from django.utils.translation import activate, get_language
from graphene_django import DjangoObjectType
from markdownify import markdownify as md

from home.models import TgBotSnippet


class SettingsNode(DjangoObjectType):
    terms_of_use_link = graphene.String()

    class Meta:
        model = TgBotSnippet
        only_fields = ["title", "welcome_message", "main_menu_text"]

    def resolve_terms_of_use_link(self: TgBotSnippet, info):
        return self.terms_of_use_link.full_url

    def resolve_welcome_message(self: TgBotSnippet, info):
        markdown_content = md(self.welcome_message)
        return markdown_content

    def resolve_main_menu_text(self: TgBotSnippet, info):
        markdown_content = md(self.main_menu_text)
        return markdown_content


class SettingsQuery:
    get_settings = graphene.Field(SettingsNode, lang=graphene.String(required=True))

    def resolve_get_settings(self, info, lang,  **kwargs):
        activate(lang)
        queryset = TgBotSnippet.objects.first()
        try:
            return queryset
        except TgBotSnippet.DoesNotExist:
            return None
