from django.contrib.auth.models import UserManager
from django.db.models import QuerySet
from django.utils.translation import activate

from .language_query import LanguageQuery
from .settings_query import SettingsQuery
from .user_query import UserQuery

QuerySet.localize = lambda self, info: activate(info.context.COOKIES.get("lang")) and self

UserManager.user = lambda self, info: self.get(
    tg_id=info.context.COOKIES.get("tg_id")
)
