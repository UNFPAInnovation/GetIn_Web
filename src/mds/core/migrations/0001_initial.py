# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Concept'
        db.create_table(u'core_concept', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='799095ed-75c4-4204-a279-cdaf1c2220bd', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('conceptclass', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('datatype', self.gf('django.db.models.fields.CharField')(default='string', max_length=64)),
            ('mimetype', self.gf('django.db.models.fields.CharField')(default='text/plain', max_length=64)),
            ('constraint', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Concept'])

        # Adding model 'RelationshipCategory'
        db.create_table(u'core_relationshipcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='0e858b31-d0d9-41ca-8cbb-77fbb2dadcbb', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
            ('restriction', self.gf('django.db.models.fields.CharField')(max_length=512, blank=True)),
        ))
        db.send_create_signal('core', ['RelationshipCategory'])

        # Adding model 'Relationship'
        db.create_table(u'core_relationship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='e0d566ad-ad70-48a4-9a2b-8022fd0846e1', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('from_concept', self.gf('django.db.models.fields.related.ForeignKey')(related_name='concept_related_from', to_field='uuid', to=orm['core.Concept'])),
            ('to_concept', self.gf('django.db.models.fields.related.ForeignKey')(related_name='concept_related_to', to_field='uuid', to=orm['core.Concept'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.RelationshipCategory'])),
        ))
        db.send_create_signal('core', ['Relationship'])

        # Adding model 'Device'
        db.create_table(u'core_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='04fe6a32-2c64-4d4a-8942-20131edc675f', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=36)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Device'])

        # Adding model 'Encounter'
        db.create_table(u'core_encounter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='7e8e2aff-b8d5-4d78-9a9a-d5ee2f8fb628', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('procedure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Procedure'], to_field='uuid')),
            ('observer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Observer'], to_field='uuid')),
            ('device', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Device'], to_field='uuid')),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Subject'], to_field='uuid')),
            ('concept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Concept'], to_field='uuid')),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Encounter'])

        # Adding model 'Event'
        db.create_table(u'core_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='c4b7c0b1-0313-480d-9348-dde9662c4326', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('path', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=767)),
            ('messages', self.gf('django.db.models.fields.TextField')()),
            ('duration', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('core', ['Event'])

        # Adding model 'Instruction'
        db.create_table(u'core_instruction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='de2aa59e-2781-4a3e-9594-25cedaa3154e', unique=True, max_length=36)),
            ('concept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Concept'], to_field='uuid')),
            ('predicate', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('algorithm', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('compound', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('boolean_operator', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Instruction'])

        # Adding model 'Location'
        db.create_table(u'core_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='dc33122c-5abd-4a18-b068-20f528623feb', unique=True, max_length=36)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('code', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('core', ['Location'])

        # Adding model 'Notification'
        db.create_table(u'core_notification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='cc7b1eb1-309c-4245-84ba-c51255b5f8c8', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('header', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('delivered', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Notification'])

        # Adding model 'Observation'
        db.create_table(u'core_observation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='62c62452-adf4-4441-88e0-4a4e404934fd', unique=True, max_length=36)),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Encounter'], to_field='uuid')),
            ('node', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('concept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Concept'], to_field='uuid')),
            ('value_text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value_complex', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('_complex_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('_complex_progress', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Observation'])

        # Adding unique constraint on 'Observation', fields ['encounter', 'node']
        db.create_unique(u'core_observation', ['encounter_id', 'node'])

        # Adding model 'Observer'
        db.create_table(u'core_observer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='2ea75bf9-5678-44c8-8691-9f392331934e', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Observer'])

        # Adding model 'Procedure'
        db.create_table(u'core_procedure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='50c644a4-f9af-4984-aa80-5ff9bfe11b8f', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=255)),
            ('src', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Procedure'])

        # Adding model 'Subject'
        db.create_table(u'core_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='1a963d9c-6b07-4402-90a4-86723e73ee34', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Location'], to_field='uuid', blank=True)),
            ('system_id', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
        ))
        db.send_create_signal('core', ['Subject'])

        # Adding model 'Patients'
        db.create_table(u'core_patients', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.SlugField')(default='317eec10-51f7-4c5e-8140-80a1dab0f732', unique=True, max_length=36)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('voided', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('given_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('family_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('pnumber', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('holder_pNumber', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('LMD', self.gf('django.db.models.fields.DateTimeField')()),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('education_level', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('contraceptive_use', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('ANC_status', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('ANC_visit', self.gf('django.db.models.fields.DateTimeField')()),
            ('EDD', self.gf('django.db.models.fields.DateTimeField')()),
            ('receive_sms', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('follow_up', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('CUG_status', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('bleeding', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('fever', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('swollen_feet', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('blurred_vision', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('core', ['Patients'])


    def backwards(self, orm):
        # Removing unique constraint on 'Observation', fields ['encounter', 'node']
        db.delete_unique(u'core_observation', ['encounter_id', 'node'])

        # Deleting model 'Concept'
        db.delete_table(u'core_concept')

        # Deleting model 'RelationshipCategory'
        db.delete_table(u'core_relationshipcategory')

        # Deleting model 'Relationship'
        db.delete_table(u'core_relationship')

        # Deleting model 'Device'
        db.delete_table(u'core_device')

        # Deleting model 'Encounter'
        db.delete_table(u'core_encounter')

        # Deleting model 'Event'
        db.delete_table(u'core_event')

        # Deleting model 'Instruction'
        db.delete_table(u'core_instruction')

        # Deleting model 'Location'
        db.delete_table(u'core_location')

        # Deleting model 'Notification'
        db.delete_table(u'core_notification')

        # Deleting model 'Observation'
        db.delete_table(u'core_observation')

        # Deleting model 'Observer'
        db.delete_table(u'core_observer')

        # Deleting model 'Procedure'
        db.delete_table(u'core_procedure')

        # Deleting model 'Subject'
        db.delete_table(u'core_subject')

        # Deleting model 'Patients'
        db.delete_table(u'core_patients')


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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'0dcb9dc5-b311-4345-9355-e5dcd17f2944'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.device': {
            'Meta': {'object_name': 'Device'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f6ded2cf-52a6-494f-ad8a-6b1683fd6016'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'94fba168-e9d7-4099-ae2b-0342f2258d6f'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'62a44ba3-c200-4ef3-a04e-c678206ad9bd'", 'unique': 'True', 'max_length': '36'})
        },
        'core.instruction': {
            'Meta': {'object_name': 'Instruction'},
            'algorithm': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'boolean_operator': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'compound': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Concept']", 'to_field': "'uuid'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'predicate': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'a8476a22-7b55-4da3-aae3-a369c7993c18'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.location': {
            'Meta': {'object_name': 'Location'},
            'code': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'2e5180d6-8b40-418c-ab54-fbccf44aad76'", 'unique': 'True', 'max_length': '36'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'f2f0c481-7a3e-497b-afb2-0e422aad5fa4'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'07322f45-9117-4aba-813d-e4274dda53f0'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'224d73ec-43e2-49a1-b684-9bed4aeb3f4f'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'core.patients': {
            'ANC_status': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'ANC_visit': ('django.db.models.fields.DateTimeField', [], {}),
            'CUG_status': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'EDD': ('django.db.models.fields.DateTimeField', [], {}),
            'LMD': ('django.db.models.fields.DateTimeField', [], {}),
            'Meta': {'object_name': 'Patients'},
            'bleeding': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'blurred_vision': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'contraceptive_use': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'education_level': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'fever': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'follow_up': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'holder_pNumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pnumber': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'receive_sms': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'swollen_feet': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'5987c7fc-7916-400c-84a6-8e1f05018f45'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'da277484-8d3a-4a82-baa4-9fec3217aeb8'", 'unique': 'True', 'max_length': '36'}),
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
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'52711c1a-0326-4314-a4ef-41d3b7e7f888'", 'unique': 'True', 'max_length': '36'})
        },
        'core.relationshipcategory': {
            'Meta': {'object_name': 'RelationshipCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'restriction': ('django.db.models.fields.CharField', [], {'max_length': '512', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'7f6c4115-8781-470d-91c5-0beae05d93ce'", 'unique': 'True', 'max_length': '36'})
        },
        'core.subject': {
            'Meta': {'object_name': 'Subject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'given_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Location']", 'to_field': "'uuid'", 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'system_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.SlugField', [], {'default': "'2a72eae3-ec40-420c-84c9-bd8394558ae9'", 'unique': 'True', 'max_length': '36'}),
            'voided': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['core']