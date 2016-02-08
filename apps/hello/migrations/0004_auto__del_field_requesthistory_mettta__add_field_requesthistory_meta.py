# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RequestHistory.mettta'
        db.delete_column(u'hello_requesthistory', 'mettta')

        # Adding field 'RequestHistory.meta'
        db.add_column(u'hello_requesthistory', 'meta',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RequestHistory.mettta'
        db.add_column(u'hello_requesthistory', 'mettta',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=256),
                      keep_default=False)

        # Deleting field 'RequestHistory.meta'
        db.delete_column(u'hello_requesthistory', 'meta')


    models = {
        u'hello.mydata': {
            'Meta': {'object_name': 'MyData'},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'hello.requesthistory': {
            'Meta': {'object_name': 'RequestHistory'},
            'get': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'request_url': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['hello']