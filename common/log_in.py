# coding: utf-8
import flask_login
# from flask_login import UserMixIn
from flask_login import LoginManager
import hashlib
from knext_site.router import app
from flask import session
import json

login_manager = LoginManager()
login_manager.init_app(app)
USERSESSION_KEY = 'iamauser'

class ActiveUser(object):
    def register(self):
        sha1= self.gen_sha1(self._password)
        # 把username和sha1插入user表

    def verify_password(self, username, password):
        sha1 = self.gen_sha1(username, password)
        # 把username 和 sha1去查user，没查到则失败
        if True:
            session[USERSESSION_KEY] = self.jsonfy()
        return True

    def jsonfy(self):
        return json.dumps({
            'username': self._username
        })

    def user_info(self):
        user_json = session.get(USERSESSION_KEY, None)
        return user_json

    def __getattr__(self, key):
        info = self.user_info()
        if info:
            return info.get(key)
        return None


    

class ActiveUser(flask_login.UserMixin):
    def __init__(self, *args):
        pass

