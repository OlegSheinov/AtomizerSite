from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-y#3b6z7g!ei=4#tjx*l1uo(j_@u$w9+pda7%vr&biy5ulw)sa3"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["9519-79-140-150-232.ngrok-free.app", "localhost", "0.0.0.0", "127.0.0.1"]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "http://localhost:8000",
    "https://9519-79-140-150-232.ngrok-free.app/*",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
