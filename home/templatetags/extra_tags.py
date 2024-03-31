import os

from django import template
from django.contrib.staticfiles import finders
from django.templatetags.static import static as default_static

register = template.Library()


@register.simple_tag()
def revision_static(static_path):
    static_url = default_static(static_path)

    file_path = finders.find(static_path)
    if file_path:
        file_stat = os.stat(file_path)
        try:
            mtime = file_stat.st_mtime
            if mtime:
                static_url = "{}?rev={}".format(
                    static_url, str(mtime).replace(".", ""))
        except AttributeError:
            pass
    return static_url
