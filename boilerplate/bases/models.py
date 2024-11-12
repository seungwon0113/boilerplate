from django.db import models
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class Model(TimeStampedModel, models.Model):
    is_active = models.BooleanField(_("활성화 여부"), default=True, blank=True, null=True)

    class Meta:
        abstract = True

    objects = models.Manager()
    available = AvailableManager()
