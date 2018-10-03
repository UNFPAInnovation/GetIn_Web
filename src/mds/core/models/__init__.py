"""
Data models for the core Sana data engine. These should be extended as 
required. 

:Authors: Sana dev team
:Version: 2.0
"""

from .concept import Concept, Relationship, RelationshipCategory
from .device import Device
from .encounter import Encounter
from .events import Event
from .instruction import Instruction
from .location import *
from .notification import Notification
from .observation import Observation
from .observer import Observer
from .procedure import Procedure
from .subject import Subject
from .patients import Patients
#from .patient import Patient
from .ambulancedriver import AmbulanceDriver
from .sms_message import SMSMessage
from mds.core.extensions.models import *
from mds.core import signals

from django.db.models.signals import pre_save

pre_save.connect(signals.prepare_charfields, sender=Location)
pre_save.connect(signals.prepare_charfields, sender=Parish)
pre_save.connect(signals.prepare_charfields, sender=Subcounty)
pre_save.connect(signals.prepare_charfields, sender=County)
pre_save.connect(signals.prepare_charfields, sender=District)
pre_save.connect(signals.prepare_charfields, sender=Patients)
pre_save.connect(signals.prepare_charfields, sender=Observer)
pre_save.connect(signals.prepare_charfields, sender=AmbulanceDriver)

__all__ = ['Concept', 'Relationship','RelationshipCategory',
           'Device', 
           'Encounter',
           'Event',
           'Instruction',
           'Location',
           'Notification', 
           'Observation', 
           'Observer',
           'Parish',
           'Procedure',
           'Subcounty',
           'Subject',
           'Patients',
           'AmbulanceDriver',
           'County',
           'District',
           'SMSMessage'
           #'Patient'
           ]
