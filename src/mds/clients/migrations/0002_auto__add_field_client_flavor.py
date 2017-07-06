# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Client.flavor'
        db.add_column(u'clients_client', 'flavor',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=32, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Client.flavor'
        db.delete_column(u'clients_client', 'flavor')


    models = {
        u'clients.client': {
            'Meta': {'object_name': 'Client'},
            'app': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'flavor': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['clients']