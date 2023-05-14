import datetime

from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now

from localflavor.us.models import (
    PhoneNumberField,
    USZipCodeField,
    USStateField,
)


class Event(models.Model):
    event_admin = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE,
                                    null=True)
    name = models.CharField(max_length=255,verbose_name='НАЗВАНИЕ')
    datetime = models.DateTimeField(default=now, blank=True)
    description = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    gps_loc = models.CharField(blank=True, max_length=255)
    duration = models.CharField(blank=True,max_length=255)

    def __str__(self):
        return f'{self.name} ({self.datetime})'

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


class EventParticipant(models.Model):
    fio = models.CharField(max_length=255)
    login = models.CharField(blank=True,max_length=255)
    group = models.CharField(max_length=255, blank=True)
    gps = models.CharField(max_length=255, blank=True)
    event = models.ForeignKey(Event, null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name or ""} ({self.email or "[No Email Given]"})'
