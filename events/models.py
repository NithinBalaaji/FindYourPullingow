from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
from groups.models import Group


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    content = models.TextField()
    date_event = models.DateField()
    time_event = models.TimeField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, related_name='posts', null=True, blank=True)


    def __str__(self):
              return self.event_name

    def get_absolute_url(self):
         return reverse('event-detail',kwargs={'pk': self.pk})