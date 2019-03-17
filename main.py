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

from flask import Flask
from flask import render_template
from flask import redirect

from google.appengine.api import users
from google.appengine.ext import ndb

from controllers import group, contact, signup
from models import Group, Contact, User

from users import login

app = Flask(__name__)
app.debug = True

app.register_blueprint(contact.app)
app.register_blueprint(group.app)
app.register_blueprint(signup.app)

@app.route('/')
def index():
    context = login()

    if context.get('user') and not context.get('profile'):
        return redirect('/signup')

    return render_template('index.html', context=context)



