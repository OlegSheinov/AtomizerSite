from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from .base import BaseSnippet

help_main_menu = """
Подсказка возможных переменных в тексте:\n
$tariff - название тарифа юзера\n
$tgFirstName - его имя в тг\n
$tgId - его id в тг\n
$tgLastName - его фамилия в тг\n
$tgUsername - его юзернейм в тг\n
$timeWithUs - время пользования ботом\n
$totalUses - общее количество пользований ботом\n
$usesLeft - оставшееся количество пользований ботом\n
"""


class TgBotSnippet(BaseSnippet):
    title = models.CharField(max_length=64, blank=False, null=False, verbose_name=_("Bot name"))
    description = RichTextField(max_length=1024, blank=True, null=True, verbose_name=_("Bot description text"))
    about_bot = RichTextField(max_length=1024, blank=True, null=True, verbose_name=_("Bot about text"))
    welcome_message = RichTextField(blank=False, null=True, verbose_name=_('Welcome message on tg bot'))
    language_choice_text = RichTextField(blank=False, null=True, verbose_name=_("Language choice text"))
    tariff_choice_text = RichTextField(blank=False, null=True, verbose_name=_("Tariff choice text"))
    terms_of_use_text = RichTextField(blank=False, null=True, verbose_name=_('Terms of use text'),
                                      help_text=_('The link in the bot will be located under the texts'))
    success_payment_text = RichTextField(blank=False, null=True, verbose_name=_('Success payment text'))
    terms_of_use_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Terms of use link")
    )
    main_menu_text = RichTextField(blank=False, null=True, verbose_name=_("Main menu text"), help_text=help_main_menu)
    web_app_btn_text = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Web app button text"))
    settings_btn_text = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Settings button text"))
    tariffs_btn_text = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Tariffs button text"))
    donate_btn_text = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Donate button text"))
    home_btn_text = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Home button text"))
    back_btn_text = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Back button text"))
    buy_tariff_btn = models.CharField(max_length=32, blank=False, null=True, verbose_name=_("Buy tariff button"))

    panels = [
        FieldPanel("title"),
        FieldPanel("description"),
        FieldPanel("about_bot"),
        FieldPanel("welcome_message"),
        FieldPanel("language_choice_text"),
        FieldPanel("tariff_choice_text"),
        FieldPanel("terms_of_use_text"),
        FieldPanel("terms_of_use_link"),
        FieldPanel("main_menu_text"),
        FieldPanel("success_payment_text"),
        FieldPanel("web_app_btn_text"),
        FieldPanel("settings_btn_text"),
        FieldPanel("tariffs_btn_text"),
        FieldPanel("donate_btn_text"),
        FieldPanel("home_btn_text"),
        FieldPanel("back_btn_text"),
        FieldPanel("buy_tariff_btn"),
    ]

    class Meta:
        verbose_name = _('Bot settings')
        verbose_name_plural = _("Bot settings")

    def __str__(self):
        return self.title
