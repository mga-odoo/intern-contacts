# -*- coding: utf-8 -*-
#!/usr/bin/env python

from google.appengine.ext import ndb
from google.appengine.api import users

from models import User

def login():
    url = url_linktext = profile = False
    context = {}

    if users.get_current_user():
        url = users.create_logout_url('/')
        profile = User.query(User.user == users.get_current_user())
        profile = profile.fetch(limit=1)
        if profile:
            context.update({
                'profile': profile[0]
            })
    else:
        url = users.create_login_url('/')

    context.update({
        'url': url,
        'user': users.get_current_user(),
        'is_admin': users.is_current_user_admin()
    })

    return context
