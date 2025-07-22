from django.db import models
from django.utils import timezone


class Authenticator(models.Model):
    auth_name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    fullـaccess = models.BooleanField()
    server_name = models.CharField(max_length=200, null=False, blank=False)
    IPـaddress = models.GenericIPAddressField(
        protocol="IPv4", unpack_ipv4=False)
    create_date = models.DateTimeField("date created", default=timezone.now)
    description = models.CharField(max_length=1000)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return '%s(%s) - %s' % (self.auth_name, self.create_date, self.description)
