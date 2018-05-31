""" An entity about whom data is collected.

:Authors: Sana dev team
:Version: 2.0
"""
from django.db import models
from mds.api.utils import make_uuid

__all__ = ["SMSMessage",]

class SMSMessage(models.Model):
    """ Reusable sms messages. """
    class Meta:
        app_label = "core"

    uuid = models.SlugField(max_length=36, unique=True, default=make_uuid, editable=False)
    """ A universally unique identifier """

    tag = models.CharField(max_length=128)
    """Short identifier or label."""
    
    text = models.TextField()
    "The message body."""
    
    created = models.DateTimeField(auto_now_add=True)
    """ When the object was created """

    modified = models.DateTimeField(auto_now=True)
    """ updated on modification """

    voided = models.BooleanField(default=False)
