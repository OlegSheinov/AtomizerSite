from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from home.models import Tariffs, TgBotSnippet, HomePage


@register(Tariffs)
class TariffsTO(TranslationOptions):
    fields = (
        'name',
        'description',
    )


@register(TgBotSnippet)
class TgBotSnippetTO(TranslationOptions):
    fields = (
        "welcome_message",
        "description",
        "about_bot",
        "language_choice_text",
        "tariff_choice_text",
        "main_menu_text",
        "success_payment_text",
        "terms_of_use_text",
        "web_app_btn_text",
        "settings_btn_text",
        "tariffs_btn_text",
        "donate_btn_text",
        "home_btn_text",
        "back_btn_text",
        "buy_tariff_btn",
    )


@register(HomePage)
class HomePageTO(TranslationOptions):
    fields = ('header', )
