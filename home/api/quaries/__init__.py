from django.contrib.auth.models import UserManager

from .language_query import LanguageQuery
from .settings_query import SettingsQuery
from .user_query import UserQuery

UserManager.user = lambda self, info: self.get(
    tg_id=info.context.COOKIES.get("tg_id")
)
