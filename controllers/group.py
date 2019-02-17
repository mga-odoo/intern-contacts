# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from google.appengine.ext import ndb
from google.appengine.api import users

from users import login
from models import Group

app = Blueprint('group', __name__, template_folder='templates')

@app.route('/groups')
@app.route('/groups/<group>')
def index(group=None):
    context = login()
    group_all = Group.query(Group.user == users.get_current_user()).order(Group.name)
    if users.is_current_user_admin():
        group_all = Group.query().order(Group.name)
    group_edit = False

    if group:
        group_edit = ndb.Key(urlsafe=group).get()

    groups = group_all.fetch()
    return render_template('group.html', group=group_edit, groups=groups, context=context)

@app.route('/groups/create', methods=['POST'])
def create():
    group = Group()
    if request.form.get('group'):
        group = ndb.Key(urlsafe=request.form.get('group')).get()

    if request.form.get('group_name'):
        group.name = request.form.get('group_name')
        group.user = users.get_current_user()
        group.put()
    return redirect('/groups')

@app.route('/groups/drop/<group>')
def drop(group=None):
    if group:
        group_edit = ndb.Key(urlsafe=group).delete()

    return redirect('/groups')