import graphene
from graphene_django import DjangoObjectType
from wagtail.templatetags.wagtailcore_tags import richtext

from home.models import TgBotSnippet
from home.utils.html import to_html


class SettingsNode(DjangoObjectType):
    terms_of_use_link = graphene.String()

    class Meta:
        model = TgBotSnippet
        only_fields = [
            "title",
            "welcome_message",
            "main_menu_text",
            "terms_of_use_text",
            "web_app_btn_text",
            "settings_btn_text",
            "tariffs_btn_text",
            "donate_btn_text",
        ]

    def resolve_terms_of_use_link(self: TgBotSnippet, info):
        return self.terms_of_use_link.full_url

    def resolve_welcome_message(self: TgBotSnippet, info):
        return to_html(richtext(self.welcome_message))

    def resolve_main_menu_text(self: TgBotSnippet, info):
        return to_html(richtext(self.main_menu_text))

    def resolve_terms_of_use_text(self: TgBotSnippet, info):
        return to_html(richtext(self.terms_of_use_text))


class SettingsQuery:
    get_messages = graphene.Field(SettingsNode)

    def resolve_get_messages(self, info, **kwargs):
        queryset = TgBotSnippet.objects.first()
        try:
            return queryset
        except TgBotSnippet.DoesNotExist:
            return None
