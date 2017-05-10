# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Observer.subcounty'
        db.add_column(u'core_observer', 'subcounty',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Subcounty'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Observer.subcounty'
        db.delete_column(u'core_observer', 'subcounty_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.ambulancedriver': {
            'Meta': {'object_name': 'AmbulanceDriver'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'subcounty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Subcounty']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'22aba011-cafe-4b55-902d-4976cb037bbc'", 'max_length': '36'})
        },
        'core.concept': {
            'Meta': {'object_name': 'Concept'},
            'conceptclass': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'constraint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'datatype': ('django.db.models.fields.CharField', [], {'default': "'string'", 'max_length': '64'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'default': "'text/plain'", 'max_length': '64'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'7040cdce-52e9-4768-b2fb-2625823cf56d'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.device': {
            'Meta': {'object_name': 'Device'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'e563100e-7a5b-4265-86cb-f600518272af'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.encounter': {
            'Meta': {'object_name': 'Encounter'},
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Concept']", 'to_field': "'uuid'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'device': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Device']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'observer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Observer']", 'to_field': "'uuid'"}),
            'procedure': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Procedure']", 'to_field': "'uuid'"}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Subject']", 'to_field': "'uuid'"}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'b1390af4-fedd-432c-b7f2-9d2effd54d43'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.event': {
            'Meta': {'object_name': 'Event'},
            'client': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'messages': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '767'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'21c9955c-b8f8-4679-8d69-9b0799e3a3f5'", 'unique': 'True', 'max_length': '36'})
        },
        'core.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'algorithm': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'boolean_operator': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Concept']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predicate': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'7eeef0de-42fe-412e-9c76-fe31753480c1'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'code': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Parish']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'b7cbbcea-6b94-449e-b25e-8a183bf6520e'", 'unique': 'True', 'max_length': '36'})
        },
        'core.notification': {
            'Meta': {'object_name': 'Notification'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delivered': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'header': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'df35d51d-5c0b-45a5-8851-08e8286496e0'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.observation': {
            'Meta': {'ordering': "['-created']", 'unique_together': "(('encounter', 'node'),)", 'object_name': 'Observation'},
            '_complex_progress': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            '_complex_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Concept']", 'to_field': "'uuid'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Encounter']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'node': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'98d43c64-5ce3-4511-a41a-5892da6266a6'", 'unique': 'True', 'max_length': '36'}),
            'value_complex': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'value_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.observer': {
            'Meta': {'object_name': 'Observer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Location']", 'symmetrical': 'False', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '64'}),
            'subcounty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Subcounty']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'b6796b40-a118-43a6-a32c-fd3fa2b589ce'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.parish': {
            'Meta': {'object_name': 'Parish'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subcounty': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Subcounty']"})
        },
        'core.patients': {
            'Meta': {'object_name': 'Patients', '_ormbases': ['core.Subject']},
            'ambulance_need': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3', 'blank': 'True'}),
            'ambulance_response': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3', 'blank': 'True'}),
            'anc_status': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60', 'blank': 'True'}),
            'anc_visit': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'bleeding': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60', 'blank': 'True'}),
            'blurred_vision': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contraceptive_use': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60'}),
            'county': ('django.db.models.fields.CharField', [], {'default': "'Not Specified'", 'max_length': '128', 'blank': 'True'}),
            'cug_status': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'default': "'Not Specified'", 'max_length': '128', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'edd': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'education_level': ('django.db.models.fields.CharField', [], {'default': "'Primary_level'", 'max_length': '60', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'fever': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60', 'blank': 'True'}),
            'follow_up': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'holder_pnumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'lmd': ('django.db.models.fields.DateTimeField', [], {}),
            'location': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'default': "'SINGLE'", 'max_length': '64'}),
            'parish': ('django.db.models.fields.CharField', [], {'default': "'Not Specified'", 'max_length': '128', 'blank': 'True'}),
            'pnumber': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'receive_sms': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60'}),
            'subcounty': ('django.db.models.fields.CharField', [], {'default': "'Not Specified'", 'max_length': '128', 'blank': 'True'}),
            u'subject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Subject']", 'unique': 'True', 'primary_key': 'True'}),
            'swollen_feet': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '60', 'blank': 'True'}),
            'village': ('django.db.models.fields.CharField', [], {'default': "'Not Specified'", 'max_length': '128', 'blank': 'True'})
        },
        'core.procedure': {
            'Meta': {'object_name': 'Procedure'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'src': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'c7fce523-37b3-4af8-9d6e-9280c97224b1'", 'unique': 'True', 'max_length': '36'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '255'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.relationship': {
            'Meta': {'object_name': 'Relationship'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.RelationshipCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_concept': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concept_related_from'", 'to_field': "'uuid'", 'to': "orm['core.Concept']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'to_concept': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concept_related_to'", 'to_field': "'uuid'", 'to': "orm['core.Concept']"}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f12d17ed-ca18-4237-88ad-753054c02a5d'", 'unique': 'True', 'max_length': '36'})
        },
        'core.relationshipcategory': {
            'Meta': {'object_name': 'RelationshipCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'restriction': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'50eb9025-d715-4414-8944-861efa655608'", 'unique': 'True', 'max_length': '36'})
        },
        'core.subcounty': {
            'Meta': {'object_name': 'Subcounty'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.subject': {
            'Meta': {'object_name': 'Subject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'6c1075d0-8886-4565-9187-ff42a7ac7274'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['core']