# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask, render_template

from google.appengine.api import users
from google.appengine.ext import ndb

from controllers import group, contact
from models import Group, Contact

from users import login

app = Flask(__name__)
app.debug = True

app.register_blueprint(contact.app)
app.register_blueprint(group.app)

@app.route('/')
def index(group_key=None):
    context = login()
    return render_template('index.html', context=context)

    # context = login()
    # group = Group.query(Group.user == users.get_current_user()).order(Group.name)
    # groups = group.fetch()

    # contact = Contact.query(Contact.user == users.get_current_user()).order(Contact.name)
    # if group_key:
    #     contact = Contact.query(Contact.user == users.get_current_user() 
    #             and Contact.group == ndb.Key(urlsafe=group_key)).order(Contact.name)
    # contacts = contact.fetch()

    # return render_template('index.html',  groups=groups, contacts=contacts,vals=context)
