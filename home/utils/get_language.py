from django.conf import settings


def get_allowed_languages():
    return settings.ALLOWED_LANGUAGES