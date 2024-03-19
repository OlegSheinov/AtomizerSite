from django.apps import apps
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseSnippet(models.Model):
    class Meta:
        abstract = True

    def clean(self):
        super().clean()
        my_model = apps.get_model(self._meta.label)
        existing_count = my_model.objects.count()
        max_instances = 1
        if existing_count >= max_instances and self._state.adding:
            raise ValidationError(_(f"Может быть только {max_instances} экземпляр(ов) сниппета {self.__str__()}."))
