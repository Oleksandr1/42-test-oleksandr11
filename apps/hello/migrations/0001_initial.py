# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MyData'
        db.create_table(u'hello_mydata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('biography', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'hello', ['MyData'])

        # Adding model 'RequestHistory'
        db.create_table(u'hello_requesthistory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('get', self.gf('django.db.models.fields.TextField')()),
            ('meta', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('s', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'hello', ['RequestHistory'])


    def backwards(self, orm):
        # Deleting model 'MyData'
        db.delete_table(u'hello_mydata')

        # Deleting model 'RequestHistory'
        db.delete_table(u'hello_requesthistory')


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
            'meta': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'request_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            's': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'})
        }
    }

    complete_apps = ['hello']
