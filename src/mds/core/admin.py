"""Sana mDS Django admin interface

:Authors: Sana dev team
:Version: 2.0
"""

from django.contrib import admin
from .models import *
"""from mds.core.models.patients import Subject
""" 

def mark_voided(modeladmin,request,queryset):
    queryset.update(voided=True)
mark_voided.short_description = "Mark selected voided"

class DeviceAdmin(admin.ModelAdmin):
    readonly_fields = ['uuid']  
    list_display = ['name', 'uuid']
    list_filter = ['name',]
    actions=[mark_voided,]

class ProcedureAdmin(admin.ModelAdmin):
    readonly_fields = ['uuid']
    list_display = ['title', 'author', 'uuid']
    actions=[mark_voided,]

class RestAdmin(admin.TabularInline):
    app_label="REST Services"
    inlines = []

class RelationshipAdmin(admin.TabularInline):
    model = Relationship
    fk_name = 'to_concept'
    list_display_links = []
    
class ConceptAdmin(admin.ModelAdmin):
    inlines = [ 
        RelationshipAdmin,
        ]
    readonly_fields = ['uuid']  
    list_display = ['name', 'uuid']
    list_filter = ['name',]
    actions=[mark_voided,]

class ObservationAdmin(admin.ModelAdmin):
    exclude = ('_complex_progress',)
    readonly_fields = ['_complex_size','uuid','value']
    list_display = ['question','voided','concept','value', 
        'subject','device','created','modified', 'encounter', 'upload_progress']
    list_filter = ['node','concept', 'modified' ]
    actions=[mark_voided,]

class EncounterAdmin(admin.ModelAdmin):
    def patient(self):
        return Patients.objects.get(uuid=self.subject)
        
    #exclude = ['concept',]
    list_display = [ 'subject','voided','concept', 'procedure', 'created','uuid',"observer",]
    #actions = [mark_encounter_voided,]
    actions=[mark_voided,]
    readonly_fields = ['uuid',]

class EncounterInline(admin.StackedInline):
    model = Encounter

class ObserverAdmin(admin.ModelAdmin):
    readonly_fields = ['uuid',]
    list_display = ['user', 'uuid', 'role']
    actions=[mark_voided,]


class SubjectAdmin(admin.ModelAdmin):
    readonly_fields = ['uuid',]
    list_display = ['given_name', 'family_name', 'uuid', "image"]

class SubjectInline(admin.StackedInline):
    model = Subject

class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ('name', 'uuid')
    list_filter = ('name',)
    
class EventAdmin(admin.ModelAdmin):
    model = Event
class PatientAdmin(admin.ModelAdmin):
    model=Patients
    list_display = ['given_name', 'family_name', 'uuid','village', 'system_id']
class AmbulanceDriverAdmin(admin.ModelAdmin):
    model = AmbulanceDriver
    list_display = [
        'first_name',
        'last_name', 
        'phone_number',
        'subcounty',
        'uuid'
    ]
    
class ParishAdmin(admin.ModelAdmin):
    model = Parish
    list_display = [
        'name',
        'subcounty'
    ]

class SubcountyAdmin(admin.ModelAdmin):
    model = Subcounty
    list_display = [
        'name',
    ]

class CountyAdmin(admin.ModelAdmin):
    model = County
    list_display = [
        'name',
        'district'
    ]

class DistrictAdmin(admin.ModelAdmin):
    model = District
    list_display = [
        'name',
    ]

class SMSMessageAdmin(admin.ModelAdmin):
    model = SMSMessage
    list_display = [
        'tag',
    ]

admin.site.register(Concept, ConceptAdmin)
admin.site.register(Relationship)
admin.site.register(RelationshipCategory)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Encounter, EncounterAdmin)
admin.site.register(Observation,ObservationAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Notification)
admin.site.register(Observer,ObserverAdmin)
admin.site.register(Procedure,ProcedureAdmin)
admin.site.register(Patients, PatientAdmin)
admin.site.register(Event)
admin.site.register(AmbulanceDriver, AmbulanceDriverAdmin)
admin.site.register(Parish, ParishAdmin)
admin.site.register(Subcounty, SubcountyAdmin)
admin.site.register(County, CountyAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(SMSMessage, SMSMessageAdmin)
#admin.site.register(ClientEventLog, ClientEventLogAdmin)
