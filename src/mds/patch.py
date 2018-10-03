import os
import re
import datetime
import inspect
from mds.core.models import *

villages = [
    'Nduguto ',
    'BUBURONGU CENTRAL ',
    'SAARA CITY ',
    'DUMBA ',
    'NYAKAKAINDO I ',
    'MUKUNDUNGU WEST ',
    'KINYANTE CENTRAL ',
    'KALERA ',
    'NYAHUKA CENTRAL ',
    'HAMUTOMA CENTRAL ',
    'BUGHALAMA II ',
    'BUBOMBOLI CENTRAL ',
    'BUNDIKAHUNGU NORTH ',
    'BUNDIKAKEMBA WEST ',
    'TWANZANE CENTRAL ',
    'BUNGUHA CENTRAL ',
    'BUMAGA I ',
    'BUNDIMASOLI CENTRAL ',
    'BUNDIMASOLI WEST ',
    'KABALE CENTRAL ',
    'BUNDIMWALI  ',
    'KIRUMYA T.C.',
    'NGARAM 1',
    'RUGARAMA ',
    ' MUNYANGA CELL',
    ' KIREHE'
    ]

def recreate(locations=villages):
    for location in locations:
        stripped = location.strip()
        try:
            obj = Location.objects.get(name__iexact=stripped)
            print("'{}' => '{}'".format(obj.name, location))
            obj.name = location
            obj.save()
        except Exception as e:
            print("{} => '{}'".format(e, location))
        #obj.save()

def fixname(model, name):
    fixed = name.strip().upper()
    if not fixed == name:
        print("Updating {} '{}' => '{}'".format(model, name, fixed))
    return fixed

_llog = "/opt/sana/sana.mds/cache/logs/patch_locality.log"
_lelog = "/opt/sana/sana.mds/cache/logs/patch_locality.log"
_plog = "/opt/sana/sana.mds/cache/logs/patch_patients.log"
_pelog = "/opt/sana/sana.mds/cache/logs/patch_patients_errors.log"


def fqn(obj):
    name = ''
    module =  obj.__module__
    # obj is class
    if inspect.isclass(obj):
        name = obj.__name__
    # obj instance of class
    else:
        name = obj.__class__.__name__
    return '{}.{}'.format(module, name)

def write_logs(logs, f):
    if not os.path.exists(os.path.dirname(f)):
        try:
            os.makedirs(os.path.dirname(f))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
    # write to the logs
    with open(f,"a+") as logfile:
        for log in logs:
            logfile.write(log)

def patch_localities():
    logs = []
    errors = []
    models = [
        Location,
        Parish,
        Subcounty,
        County,
        District
    ]
    # strips the whitespace from the name fields
    for model in models:
        for obj in model.objects.all():
            try:
                fixed = fixname(model, obj.name)
                if not fixed == obj.name:
                    log = "{},{},'{}','{}'\n".format(fqn(obj), obj.id, obj.name, fixed)
                    obj.name = fixed
                    obj.save()
                    logs.append(log)
                else:
                    print('recreate skipping {} => {}'.format(fqn(obj), obj.name))
            except Exception as e:
                errors.append("{},{},{},'{}','{}'\n".format(e, fqn(model), obj.id, obj.name, fixed))
    if logs:
        write_logs(logs, _llog)
    if errors:
        write_logs(errors, _lelog)

def patch_patients():
    errors = []
    logs = []
    # correct patient village/location issue
    regex = re.compile(r'^[A-Z]')
    for obj in Patients.objects.all():
        # fix village and then cascade up
        if not obj.village:
            location = obj.location
            if obj.location:
                name = fixname(obj, obj.location)
                if name:
                    if regex.match(name):#name.startswith("("):
                        logs.append("'{}','{}','{}','{}'\n".format(fqn(obj), obj.id,village, name))
                        obj.village = name
                    else:
                        errors.append("{} location not fixable..'{}' '{}' '{}' village='{}'\n".format(fqn(obj), obj.family_name, obj.given_name, obj.id, name))
        else:
            name = fixname(obj, obj.village)
            obj.village = name
        obj.save()
        village = obj.village
        location = None;
        '''
        try:
        
            
            location = Location.objects.get(name=village)
            if not obj.parish:
                obj.parish = location.parish.name
            if not obj.subcounty:
                obj.subcounty = location.parish.subcounty
            if not obj.county:
                pass
            if not obj.district:
                obj.district = location.parish.subcounty.district.name
            obj.save()
        except Exception as e:
            #errors.append("'{}','{}','{}','{}'\n".format(e,obj.id, obj.uuid, village))
            continue
        '''
                
    if logs:
        write_logs(logs, _plog)
    if errors:
        write_logs(errors, _pelog)
def patch():
    patch_localities()
    patch_patients()

