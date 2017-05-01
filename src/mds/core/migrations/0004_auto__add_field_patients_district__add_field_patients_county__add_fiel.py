# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Patients.district'
        db.add_column(u'core_patients', 'district',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Patients.county'
        db.add_column(u'core_patients', 'county',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Patients.subcounty'
        db.add_column(u'core_patients', 'subcounty',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Patients.parish'
        db.add_column(u'core_patients', 'parish',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)

        # Adding field 'Patients.village'
        db.add_column(u'core_patients', 'village',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Patients.district'
        db.delete_column(u'core_patients', 'district')

        # Deleting field 'Patients.county'
        db.delete_column(u'core_patients', 'county')

        # Deleting field 'Patients.subcounty'
        db.delete_column(u'core_patients', 'subcounty')

        # Deleting field 'Patients.parish'
        db.delete_column(u'core_patients', 'parish')

        # Deleting field 'Patients.village'
        db.delete_column(u'core_patients', 'village')


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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'4f5d547b-cb46-4a81-8054-b7ebd3894a6c'", 'max_length': '36'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'286d8dcf-9350-4d6d-a869-1ec772b482b4'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.device': {
            'Meta': {'object_name': 'Device'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f034f32b-e667-4618-891e-229c9d7b74f6'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'e7d38ca7-0097-4e93-af9e-d100ac9cdfd9'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'cf4bff3d-0b71-440e-9014-7d5fcb81dfea'", 'unique': 'True', 'max_length': '36'})
        },
        'core.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'algorithm': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'boolean_operator': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Concept']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predicate': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'6ec4b676-9d3e-4842-b3bb-519710b08c7f'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'code': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'7cac222b-abb7-478b-a59e-8c8c73fcc60b'", 'unique': 'True', 'max_length': '36'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'c37bf15a-fcf3-45c4-a60d-4e97daae14b1'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'6e19f9c5-0959-4ff4-b5cb-bcbd9db2f368'", 'unique': 'True', 'max_length': '36'}),
            'value_complex': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'value_text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.observer': {
            'Meta': {'object_name': 'Observer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f988eab6-70ee-4bac-b63c-5a0dd2546f18'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.patients': {
            'Meta': {'object_name': 'Patients', '_ormbases': ['core.Subject']},
            'anc_status': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'anc_visit': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'bleeding': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'blurred_vision': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'contraceptive_use': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'cug_status': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'edd': ('django.db.models.fields.DateTimeField', [], {}),
            'education_level': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'fever': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'follow_up': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'holder_pnumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'lmd': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'parish': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'pnumber': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'receive_sms': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'subcounty': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            u'subject_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['core.Subject']", 'unique': 'True', 'primary_key': 'True'}),
            'swollen_feet': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'village': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'d510b73c-0923-4d8a-b138-b6a258cb213d'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'358f139d-4547-4183-9b23-f45106cd57f9'", 'unique': 'True', 'max_length': '36'})
        },
        'core.relationshipcategory': {
            'Meta': {'object_name': 'RelationshipCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'restriction': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'6e020dac-4f5a-4b55-af69-f6d5592b9621'", 'unique': 'True', 'max_length': '36'})
        },
        'core.subject': {
            'Meta': {'object_name': 'Subject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'54d3d39c-d39f-4a88-9717-2ef886e00906'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['core']