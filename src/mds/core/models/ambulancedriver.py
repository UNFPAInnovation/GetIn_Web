from django.db import models

from mds.api.utils import make_uuid

class AmbulanceDriver(models.Model):
    class Meta:
        app_label = "core"

    uuid = models.SlugField(max_length=36, default=make_uuid)
    phone_number = models.CharField(max_length=10)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
