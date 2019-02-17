# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

from google.appengine.api.mail import EmailMessage
class User(ndb.Model):
    email = ndb.StringProperty(indexed=True)

    def signup(self, subject, body):
        message = EmailMessage()
        message.sender = 'mantavyagajjar@gmail.com'
        message.to = [self.email]
        message.subject = subject
        message._add_body('text/html', body)
        message.check_initialized()
        message.send()

class Group(ndb.Model):
    user = ndb.UserProperty()
    name = ndb.StringProperty(indexed=True)

    def put(self):
        return super(Group, self).put()

    def browse(self, urlsafe):
        return ndb.Key(urlsafe=urlsafe).get()
        
class Contact(ndb.Model):
    user = ndb.UserProperty()
    group = ndb.KeyProperty(kind=Group)
    name = ndb.StringProperty(indexed=True)
    email = ndb.StringProperty(indexed=True)
    phone = ndb.StringProperty(indexed=True)
    note = ndb.TextProperty(indexed=True)

    def put(self):
        res = super(Contact, self).put()
        return res

    def browse(self, urlsafe):
        return ndb.Key(urlsafe=urlsafe).get()

