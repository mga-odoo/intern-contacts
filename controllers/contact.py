# -*- coding: utf-8 -*-
#!/usr/bin/env python

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

@app.route('/contacts')
@app.route('/contacts/group/<group_key>')
def contacts_list(group_key=None):
    '''Return the page with list of contact
    Params: group_key is used to filter the contacts by groups'''

    context = login()
    group = Group.query(Group.user == users.get_current_user()).order(Group.name)
    groups = group.fetch()

    contact = Contact.query(Contact.user == users.get_current_user()).order(Contact.name)
    if group_key:
        contact = Contact.query(Contact.user == users.get_current_user() 
                and Contact.group == ndb.Key(urlsafe=group_key)).order(Contact.name)
    contacts = contact.fetch()

    return render_template('index.html',  groups=groups, contacts=contacts, context=context)

@app.route('/contacts/new')
@app.route('/contacts/edit/<contact_edit>')
def contact_new(contact_edit=None):
    '''Return the page with form to fill the contact information
    Params: contact_edit holds the contation information when contact is in edit mode'''

    context = login()
    group = Group.query(Group.user == users.get_current_user()).order(Group.name)
    groups = group.fetch()
    
    contact = False
    if contact_edit:
        contact = Contact()
        contact = contact.browse(contact_edit)
    
    return render_template('contact.html', groups=groups, contact=contact, context=context)

@app.route('/contacts/save', methods=['POST'])
def contact_save():
    '''Create or update the contact in database and redirects to the contact page'''
    contact = Contact()
    if request.form.get('contact_edit'):
        contact = contact.browse(request.form.get('contact_edit'))

    group = Group()
    if request.form.get('contact_group'):
        group = group.browse(request.form.get('contact_group'))

    contact.user = users.get_current_user()
    contact.group = group.key
    contact.name = request.form.get('contact_name')
    contact.email = request.form.get('contact_email')
    contact.phone = request.form.get('contact_phone')
    contact.note = request.form.get('contact_note')

    if contact.name and contact.email:
        contact.put()

    return redirect('/contacts')

@app.route('/contacts/drop/<contact_drop>')
def contact_drop(contact_drop=None):
    if contact_drop:
        ndb.Key(urlsafe=contact_drop).delete()

    return redirect('/contacts')