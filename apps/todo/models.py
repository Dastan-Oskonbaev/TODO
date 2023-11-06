from django.db import models

from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=200,
    )
    description = models.TextField(
        _('Description'),
    )
    completed = models.BooleanField(
        _('Completed'),
        default=False)
    created = models.DateTimeField(
        _('Created'),
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
