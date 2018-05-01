from django.db import models
from .subject import Subject

def yes_no():
    return (('Yes','Yes'),('No','No'))

_education_levels = [
    "Primary_level",
    "OLevel",
    "Alevel",
    "Tertiary"
]

def education_level_choices():
    return [(x,x) for x in _education_levels]

_marital_status = [
    "SINGLE",
    "MARRIED",
    "DIVORCED"
]
def marital_status_choices():
    return [(x,x) for x in _marital_status ]


class Patients(Subject): 
    """ Simple subject implementation as a medical patient. 
    """
    class Meta:
        app_label = "core"
        verbose_name = "pregnant girl"
    given_name = models.CharField(max_length=64)
    family_name=models.CharField(max_length=64)
    pnumber = models.CharField(max_length=10)
    dob=models.DateTimeField()
    gender=models.CharField(max_length=6)
    holder_pnumber = models.CharField(max_length=10, blank=True)
    lmd = models.DateTimeField()
    marital_status = models.CharField(choices=marital_status_choices(), default="SINGLE", max_length=64)
    comment = models.TextField(blank=True)
    location=models.TextField(blank=True)
    education_level=models.CharField(choices=education_level_choices(), 
            default="Primary_level", max_length=60, blank=True)
    contraceptive_use=models.CharField(choices=yes_no(), default="No", max_length=60)
    anc_status=models.CharField(choices=yes_no(), default="No", max_length=60, blank=True)
    anc_visit=models.DateTimeField(blank=True)
    edd=models.DateTimeField(blank=True)
    receive_sms=models.CharField(choices=yes_no(), default="No", max_length=60)
    follow_up=models.CharField(choices=yes_no(), default="No", max_length=60)
    cug_status=models.CharField(choices=yes_no(), default="No", max_length=60, blank=True)
    bleeding=models.CharField(choices=yes_no(), default="No", max_length=60, blank=True)
    fever=models.CharField(choices=yes_no(), default="No", max_length=60, blank=True)
    swollen_feet=models.CharField(choices=yes_no(), default="No", max_length=60, blank=True)
    blurred_vision=models.CharField(choices=yes_no(), default="No", max_length=60, blank=True)

    district = models.CharField(max_length=128, blank=True, default="Not Specified")
    county = models.CharField(max_length=128,blank=True, default="Not Specified")
    subcounty = models.CharField(max_length=128,blank=True, default="Not Specified")
    parish = models.CharField(max_length=128,blank=True, default="Not Specified")
    village = models.CharField(max_length=128,blank=True, default="Not Specified")

    ambulance_need  = models.CharField(choices=yes_no(), default="No", max_length=3, blank=True)
    ambulance_response  = models.CharField(choices=yes_no(), default="No", max_length=3, blank=True)

    system_id = models.CharField(max_length=64, blank=True)
