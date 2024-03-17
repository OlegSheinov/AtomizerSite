from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import TgBotSnippet, Tariffs


@register_snippet
class TgBotSettingsSnippetViewSet(SnippetViewSet):
    model = TgBotSnippet
    icon = "cogs"
    list_per_page = 1


@register_snippet
class TariffsSnippetViewSet(SnippetViewSet):
    model = Tariffs
    icon = "cogs"
    list_per_page = 10
