# -*- coding: utf-8 -*-
#!/usr/bin/env python

from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.api.mail import EmailMessage

from users import login
from models import Group
from models import User

from flask import jsonify

app = Blueprint('signup', __name__, template_folder='templates')

def signup_email(email_to, subject, body):
    message = EmailMessage()
    message.sender = 'mantavyagajjar@gmail.com'
    message.to = [email_to]
    message.subject = subject
    message._add_body('text/html', body)
    message.check_initialized()
    message.send()

@app.route('/signup')
@app.route('/profile/<profile>')
def index(profile=None):
    context = login()
    if profile:
        profile = ndb.Key(urlsafe=profile).get()
    return render_template('signup.html', profile=profile, context=context)

@app.route('/profile/notification/enable', methods=['POST'])
def notification_enable():
    context = login()
    user = User()
    result = False

    if request.form.get('profile_edit'):
        user = ndb.Key(urlsafe=request.form.get('profile_edit')).get()
        user.fcmkey = request.form.get('currentToken')
        user.put()
        result = True

    return jsonify({'result': result})

@app.route('/signup/configure', methods=['POST'])
def create():
    context = login()
    user = User()
    subject = 'Welcome to contact application!'

    if request.form.get('profile_edit'):
        user = ndb.Key(urlsafe=request.form.get('profile_edit')).get()
        subject = 'You just update your profile in contact application!'

    user.user = users.get_current_user()
    user.name = request.form.get('user_name')
    user.email = request.form.get('user_email')
    user.phone = request.form.get('user_phone')
    user.note = request.form.get('user_note')

    if user.name and user.email:
        user.put()
        email = render_template('signup-email.html', context=context)
        signup_email(user.email, subject, email)

    data = {
        'url': '/profile/%s' % (user.key.urlsafe()),
        'result': True,
        'profile_token': user.key.urlsafe()
    }

    return jsonify(data)
