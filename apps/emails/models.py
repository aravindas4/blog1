from django.core.mail import send_mail
from django.db import models

from apps.utils.models import BaseModel


class Email(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    to = models.EmailField()
    comments = models.TextField(blank=True)
    link = models.URLField(null=True, blank=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def send_email(self):
        send_mail(self.name, self.comments, self.email, [self.to], fail_silently=False)
        self.is_sent = True
        self.save()
