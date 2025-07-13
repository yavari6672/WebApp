from django.db import models
from django.utils import timezone


class App(models.Model):
    app_name = models.CharField(max_length=200, unique=True)
    create_date = models.DateTimeField("date created", default=timezone.now)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '%s(%s) - %s' % (self.app_name, self.create_date, self.description)
