# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class User(ndb.Model):
    user = ndb.UserProperty()
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    phone = ndb.StringProperty(indexed=True)
    note = ndb.TextProperty(indexed=True)
    fcmkey = ndb.TextProperty()

class Group(ndb.Model):
    user = ndb.UserProperty()
    name = ndb.StringProperty(indexed=True)

class Contact(ndb.Model):
    user = ndb.UserProperty()
    group = ndb.KeyProperty(kind=Group)
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    phone = ndb.StringProperty(indexed=True)
    note = ndb.TextProperty(indexed=True)
    color = ndb.StringProperty()