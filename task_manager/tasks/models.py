from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import StatusesModel
from django.utils.translation import gettext_lazy as _


class TimestampedModel(models.Model):
    """An abstract model with a pair of timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class TasksModel(TimestampedModel):

    name = models.CharField(max_length=150,
                            unique=True,
                            verbose_name=_('Name'))
    description = models.TextField(blank=True,
                                   verbose_name=_('Description'))
    status = models.ForeignKey(StatusesModel, on_delete=models.PROTECT,
                               blank=True, null=True,
                               related_name='statuses',
                               verbose_name=_('Status'))
    executor = models.ForeignKey(User, on_delete=models.CASCADE,
                                 blank=True, null=True,
                                 default='', related_name='executors',
                                 verbose_name=_('Executor'))
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               related_name='authors',
                               verbose_name=_('Author'))
    # labels = models.ManyToManyField(Label, through='Connection',
    #                                 through_fields=('task', 'label'),
    #                                 blank=True, related_name='labels',
    #                                 verbose_name=_('Labels'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
