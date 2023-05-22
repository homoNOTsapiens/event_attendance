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
    name = models.CharField(max_length=255,verbose_name='Название:')
    datetime = models.DateTimeField(default=now, blank=True,verbose_name='Дата и время:')
    description = models.CharField(blank=True, max_length=255,verbose_name='Описание:')
    address = models.CharField(blank=True, max_length=255,verbose_name='Адрес:')
    gps_loc = models.CharField(blank=True, max_length=255,verbose_name='GPS локация')
    duration = models.CharField(blank=True,max_length=255,verbose_name='Длительность')
    groups = models.CharField(blank=True,max_length=255,verbose_name='Группы:')

    def __str__(self):
        return f'{self.name} ({self.datetime})'

    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


class EventParticipant(models.Model):
    fio = models.CharField(max_length=255,verbose_name='ФИО:')
    login = models.CharField(blank=True,max_length=255,verbose_name='Логин:')
    group = models.CharField(max_length=255, blank=True,verbose_name='Группа:')
    gps = models.CharField(max_length=255, blank=True)
    event = models.ForeignKey(Event, null=True,verbose_name='Мероприятие:')
