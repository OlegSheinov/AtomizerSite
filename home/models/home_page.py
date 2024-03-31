from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    template = 'web_app.html'
    max_count = 1

    header = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Test"))
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Logo in site")
    )

    content_panels = Page.content_panels + [
        FieldPanel('logo'),
        FieldPanel('header'),
    ]

    subpage_types = [
    ]

    parent_page_types = [
        'wagtailcore.Page'
    ]
