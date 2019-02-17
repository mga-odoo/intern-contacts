# -*- coding: utf-8 -*-
#!/usr/bin/env python

from google.appengine.ext import ndb
from google.appengine.api import users

def login():
    url = url_linktext = False
    if users.get_current_user():
        url = users.create_logout_url('/')
    else:
        url = users.create_login_url('/')
    
    return {
        'url': url,
        'user': users.get_current_user(),
        'is_admin': users.is_current_user_admin()
    }
