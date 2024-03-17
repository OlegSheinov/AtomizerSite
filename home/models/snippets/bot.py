from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from .base import BaseSnippet


class TgBotSnippet(BaseSnippet):
    title = models.CharField(max_length=64, blank=False, null=False, verbose_name=_("Bot name"))
    welcome_message = RichTextField(blank=False, null=True, verbose_name=_('Welcome message on tg bot'))
    terms_of_use_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Terms of use link")
    )
    main_menu_text = RichTextField(blank=False, null=True, verbose_name=_("Main menu text"))

    panels = [
        FieldPanel("title"),
        FieldPanel("welcome_message"),
        FieldPanel("terms_of_use_link"),
        FieldPanel("main_menu_text"),
    ]

    class Meta:
        verbose_name = _('Bot settings')
        verbose_name_plural = _("Bot settings")

    @property
    def terms_of_use(self):
        return self.terms_of_use_link.link

    def __str__(self):
        return self.title
