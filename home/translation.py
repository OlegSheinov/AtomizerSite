from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from home.models import Tariffs, TgBotSnippet


@register(Tariffs)
class TariffsTO(TranslationOptions):
    fields = (
       'name',
       'description',
    )


@register(TgBotSnippet)
class TgBotSnippetTO(TranslationOptions):
    fields = (
       'welcome_message',
       'main_menu_text',
    )