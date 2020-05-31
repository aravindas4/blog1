import uuid

from django.db import models
from model_utils.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    created_by = models.CharField(max_length=255, null=True, blank=True)
    modified_by = models.CharField(max_length=255, null=True, blank=True)
    uuid = models.CharField(max_length=255, primary_key=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        if not self.pk:
            self.uuid = str(uuid.uuid4()).upper()[:8]

        return super().save(*args, **kwargs)
