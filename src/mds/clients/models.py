# Create your models here.
import mimetypes, os

from django.db import models


class Client(models.Model):

    version = models.CharField(max_length=255)
                                
    app = models.FileField(upload_to='clients/', blank=True,)

    flavor = models.CharField(max_length=32, 
        choices=((x,x) for x in ('vht','midwife')),
        blank=True)

class CrashReport(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=36, blank=True)
    report = models.FileField(upload_to='reports/', blank=True,)
    message = models.CharField(max_length=255, blank=True, default="None")
