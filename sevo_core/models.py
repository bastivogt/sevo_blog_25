from django.db import models
from django.utils.translation import gettext as _

from django.contrib.auth import get_user_model

User = get_user_model()

class BaseTimeStampsMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class BaseUserMixin(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name=_("User"))

    class Meta:
        abstract = True