from django.db import models
from django.utils import timezone


class App(models.Model):
    app_name = models.CharField(max_length=200, unique=True)
    create_date = models.DateTimeField("date created", default=timezone.now)
    description = models.CharField(max_length=1000)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return '%s(%s) - %s' % (self.app_name, self.description, self.create_date)


class App_Run(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    Running = models.IntegerField(default=0)
    Active = models.IntegerField(default=0)
    Total = models.IntegerField(default=0)
