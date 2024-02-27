from django.db import models
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    """An abstract model with a pair of timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class StatusesModel(TimestampedModel):

    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name=_('Name'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Statuses')
