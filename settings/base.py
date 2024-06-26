"""
Django settings for atomizer project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'wagtail_modeltranslation',
    'wagtail_modeltranslation.makemigrations',
    'wagtail_modeltranslation.migrate',
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    'wagtail.locales',
    "wagtail",
    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'graphene_django',
    "home",
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.locale.LocaleMiddleware',
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ROOT_URLCONF = "atomizer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "atomizer/templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = "atomizer.wsgi.application"

AUTH_USER_MODEL = "home.User"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_NAME', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 5432),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.DjangoModelPermissions',
    )
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

WAGTAIL_I18N_ENABLED = True

USE_L10N = True

USE_TZ = True

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
]

ALLOWED_LANGUAGES = ("en", "ru")

MODELTRANSLATION_LANGUAGES = ALLOWED_LANGUAGES

MODELTRANSLATION_DEFAULT_LANGUAGE = LANGUAGE_CODE

MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'default': (LANGUAGE_CODE,),
}

WAGTAILMODELTRANSLATION_TRANSLATE_SLUGS = False

LOCALE_PATHS = [os.path.join(PROJECT_DIR, 'locale')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Wagtail settings

WAGTAIL_SITE_NAME = "atomizer"

# Search
# https://docs.wagtail.org/en/stable/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

WAGTAILIMAGES_EXTENSIONS = ["gif", "jpg", "jpeg", "png", "webp", "svg"]
WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': ['bold', 'italic', 'ul', 'link']
        }
    },
    'secondary': {
        'WIDGET': 'some.external.RichTextEditor',
        # here you can specify another widget and set it via RichTextField(editor='secondary')
    },
    'full': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': ["h1", "h2", "h3", "h4", "h5", "h6", "italic", "bold", "ol", "ul", "hr", "link",
                         "document-link", "image", "embed", "code", "superscript", "subscript", "strikethrough",
                         "blockquote"]
        }
    }
}

# Graphene

GRAPHENE = {
    'SCHEMA': 'home.api.schema',
}
