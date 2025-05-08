from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        abstract = True


class DeleteManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(deleted_at=None)


class DeleteMixin(models.Model):
    deleted_at = models.DateTimeField(_('deleted at'), null=True, blank=True, default=None)

    allobjects = models.Manager()
    objects = DeleteManager()

    class Meta:
        abstract = True

    @property
    def is_deleted(self) -> bool:
        return bool(self.deleted_at)

    def hard_delete(self, using=None, keep_parents=False) -> None:  # noqa: ANN001, FBT002
        super().delete(using=using, keep_parents=keep_parents)

    def delete(self) -> None:
        self.deleted_at = timezone.now()
        self.save()
