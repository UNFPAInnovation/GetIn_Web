from django.db.models.signals import pre_save
from django.db.models.fields import *


__all__ = [
    "prepare_charfields",
    ]

_prepared_charfields = [
    CharField,
    TextField
    ]

_register = {}

def fullname(sender):
    if not sender.__module__ is None:
        return  '{}.{}'.format(sender.__module__, sender.__name__)
    else:
        return sender.__name__

def field_registry(sender):
    name = fullname(sender)
    fields = _register.get(name, [])
    if not _register.has_key(name):
        for f in sender._meta.fields:
            if type(f) in _prepared_charfields:
                fields.append(f.name)
        _register[name] = fields
    return fields

def prepare_charfields(sender, **kwargs):
    char_fields = field_registry(sender)
    instance = kwargs.get('instance', None) if kwargs else None
    update_fields = kwargs.get('update_fields', None) if kwargs else None
    if not instance:
        return
    for f in char_fields:
        if update_fields and not f in update_fields:
            continue
        value = getattr(instance, f, None)
        prepared_value = value.strip() if not value is None else value
        setattr(instance, f, prepared_value)

def prepare_patients(sender, **kwargs):
    instance = kwargs.get('instance', None) if kwargs else None
    if not instance:
        return
    location = instance.location
    village = instance.village
    if not instance.village:
        prepared_value = None