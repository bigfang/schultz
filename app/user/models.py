import uuid
from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from lib.models import DeleteMixin, TimestampMixin


class User(AbstractUser, TimestampMixin, DeleteMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, verbose_name='ID')
    first_name = None
    last_name = None

    REQUIRED_FIELDS: ClassVar[list[str]] = ['email']

    class Meta:
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self) -> None:
        pass

    def get_short_name(self) -> None:
        pass
