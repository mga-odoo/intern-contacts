# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random

from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from models import Group
from models import Contact
from users import login

from google.appengine.ext import ndb
from google.appengine.api import users

app = Blueprint('contacts', __name__, template_folder='templates')
colors = ['#f44336', '#ec407a', '#f44336', '#9c27b0', '#5e35b1', '#3949ab', 
    '#1e88e5', '#039be5', '#00acc1', '#00897b', '#43a047', '#7cb342', '#c0ca33'
    '#fdd835', '#ffb300', '#fb8c00', '#f4511e', '#6d4c41']

def group_list():
    group = Group.query(Group.user == users.get_current_user()).order(Group.name)
    groups = group.fetch()
    return groups

@app.route('/contacts')
@app.route('/contacts/group/<group_key>')
def contacts_list(group_key=None, available=False):
    '''Return the page with list of contact
    Params: group_key is used to filter the contacts by groups'''

    context = login()
    contact = Contact.query(Contact.user == users.get_current_user()).order(Contact.name)
    if context.get('is_admin'):
        contact = Contact.query().order(Contact.name)

    if group_key:
        contact = Contact.query(Contact.user == users.get_current_user() 
                and Contact.group == ndb.Key(urlsafe=group_key)).order(Contact.name)
    contacts = contact.fetch()

    return render_template('index.html',  groups=group_list(), contacts=contacts, context=context)

@app.route('/contacts/new')
@app.route('/contacts/edit/<contact_edit>')
def contact_new(contact_edit=None):
    '''Return the page with form to fill the contact information
    Params: contact_edit holds the contation information when contact is in edit mode'''

    context = login()
    
    contact = False
    if contact_edit:
        contact = ndb.Key(urlsafe=contact_edit).get()

    return render_template('contact.html', groups=group_list(), contact=contact, context=context)

@app.route('/contacts/save', methods=['POST'])
def contact_save():
    '''Create or update the contact in database and redirects to the contact page'''
    contact = Contact()
    if request.form.get('contact_edit'):
        contact = ndb.Key(urlsafe=request.form.get('contact_edit')).get()
       
    group = Group()
    if request.form.get('contact_group'):
        group = ndb.Key(urlsafe=request.form.get('contact_group')).get()

    contact.user = users.get_current_user()
    contact.group = group.key
    contact.name = request.form.get('contact_name')
    contact.email = request.form.get('contact_email')
    contact.phone = request.form.get('contact_phone')
    contact.note = request.form.get('contact_note')

    contact.color = random.sample(colors, 1)[0]

    if contact.name and contact.email:
        contact.put()

    return redirect('/contacts')

@app.route('/contacts/drop/<contact_drop>')
def contact_drop(contact_drop=None):
    if contact_drop:
        ndb.Key(urlsafe=contact_drop).delete()

    return redirect('/contacts')