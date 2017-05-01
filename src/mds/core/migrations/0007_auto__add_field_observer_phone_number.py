# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Observer.phone_number'
        db.add_column(u'core_observer', 'phone_number',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=12, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Observer.phone_number'
        db.delete_column(u'core_observer', 'phone_number')


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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'7bf0390a-9291-4d5b-8461-de4b31dab19e'", 'max_length': '36'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f1712d2c-b99f-455d-a340-8c5d9e646780'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.device': {
            'Meta': {'object_name': 'Device'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'734cd4b8-4ee9-4dae-a541-fdf24cd0dbf2'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'a3e4d7ee-b7c5-417a-a66d-cf327148972d'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'90f32bb0-4f4e-4d9a-b8ee-0a596a047eff'", 'unique': 'True', 'max_length': '36'})
        },
        'core.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'algorithm': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'boolean_operator': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Concept']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predicate': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'98e3f29b-7a2f-4dc2-9793-76ffd5afd6a1'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'code': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f308bdbb-fb79-416c-a2e1-5a2aa80eeba2'", 'unique': 'True', 'max_length': '36'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'41d6ccca-dcca-41ac-bfb5-aef003a92ae3'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f6985aa9-b638-4952-a43a-709ca724ca9f'", 'unique': 'True', 'max_length': '36'}),
            'value_complex': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'value_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.observer': {
            'Meta': {'object_name': 'Observer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '64'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'2d15ce5e-d52f-4009-a09d-99ae89faa178'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'4a2efdb2-dce0-47ca-bc62-8dc453fa467a'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'e98d4d8f-5719-4be5-ba6b-6ac6b9fcda9a'", 'unique': 'True', 'max_length': '36'})
        },
        'core.relationshipcategory': {
            'Meta': {'object_name': 'RelationshipCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'restriction': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'c180c199-bcfa-4469-989d-3cdaf9ad6a8e'", 'unique': 'True', 'max_length': '36'})
        },
        'core.subject': {
            'Meta': {'object_name': 'Subject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'fe9abcca-dc7e-4fab-9bc4-db0c294ed7b8'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['core']