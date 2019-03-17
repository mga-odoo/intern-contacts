# -*- coding: utf-8 -*-

from google.appengine.ext import ndb
from google.appengine.api.mail import EmailMessage

class User(ndb.Model):
    user = ndb.UserProperty()
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    phone = ndb.StringProperty(indexed=True)
    note = ndb.TextProperty(indexed=True)

    def signup_email(self, subject, body):
        message = EmailMessage()
        message.sender = 'mantavyagajjar@gmail.com'
        message.to = [self.user.email(), self.email]
        message.subject = subject
        message._add_body('text/html', body)
        message.check_initialized()
        message.send()

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
