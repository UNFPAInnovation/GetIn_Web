''' sana.core.models.location

:author: Sana Development Team
:version: 2.0
:copyright: Sana 2012, released under BSD New License(http://sana.mit.edu/license)
'''

from django.db import models
from mds.api.utils import make_uuid

__all__ = [ 'Location',
            'Parish',
            'Subcounty',
            'County',
            'District'
    ]

class Location(models.Model):
    
    class Meta:
        app_label = "core"
        verbose_name = "village"
        ordering = ['name',]
    
    uuid = models.SlugField(max_length=36, unique=True, default=make_uuid, editable=False)
    """ A universally unique identifier """
    
    name = models.CharField(max_length=255)
    """A label for identifying the location"""
    
    code = models.IntegerField(blank=True, default=0)
    parish = models.ForeignKey('Parish', blank=True, null=True)
    
    def __unicode__(self):
        return self.name

class Subcounty(models.Model):
    class Meta:
        app_label = "core"
        ordering = ['name',]
        
    name = models.CharField(max_length=255)
    district = models.ForeignKey('District', blank=True, null=True)
    uuid = models.SlugField(max_length=36, default=make_uuid)

    def __unicode__(self):
        return self.name
    
class Parish(models.Model):
    class Meta:
        app_label = "core"
        ordering = ['name',]
        
    name = models.CharField(max_length=255)
    subcounty = models.ForeignKey('Subcounty')
    uuid = models.SlugField(max_length=36, default=make_uuid)

    def __unicode__(self):
        return self.name

class District(models.Model):
    class Meta:
        app_label = "core"
        ordering = ['name',]
        
    name = models.CharField(max_length=255)
    uuid = models.SlugField(max_length=36, default=make_uuid)

    def __unicode__(self):
        return self.name

class County(models.Model):
    class Meta:
        app_label = "core"
        ordering = ['name',]
        
    name = models.CharField(max_length=255)
    district = models.ForeignKey('District')
    uuid = models.SlugField(max_length=36, default=make_uuid)

    def __unicode__(self):
        return self.name
