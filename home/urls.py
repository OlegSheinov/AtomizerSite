from django.urls import path

from home.api.views import GetBotSettingsAPI

app_name = 'api'
urlpatterns = [
    path("bot_setting/", GetBotSettingsAPI.as_view(), name='settings'),
]