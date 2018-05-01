"""
The observation model for the Sana data engine.

:Authors: Sana dev team
:Version: 2.0
"""

from django.db import models

from django.contrib.auth.models import User
from mds.api.utils import make_uuid

class Observer(models.Model):
    """ The user who executes the Procedure and collects the Observations """

    class Meta:
        app_label = "core"
        
    uuid = models.SlugField(max_length=36, unique=True, default=make_uuid, editable=False)
    """ A universally unique identifier """
    
    created = models.DateTimeField(auto_now_add=True)
    """ When the object was created """
    
    modified = models.DateTimeField(auto_now=True)
    """ updated on modification """

    user = models.OneToOneField(User, unique=True)
    """ A universally unique identifier. See  """

    voided = models.BooleanField(default=False)

    role = models.CharField(max_length=64,
        choices=(
          ("vht","vht"),
          ("midwife","midwife"),
          ("admin","admin"),
          ("none","none")
          ),
        default="none")

    phone_number = models.CharField(max_length=12, blank=True)

    locations = models.ManyToManyField('core.Location', blank=True)

    subcounty = models.ForeignKey('core.Subcounty', blank=True, null=True)

    parishes = models.ManyToManyField('core.Parish', blank=True, null=True)

    district = models.ForeignKey('core.District', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.user)
