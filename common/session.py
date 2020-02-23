from flask import session
from flask_session import Session
from knext_site.router import app
import redis


app.config['SECRET_KEY'] = 'ykgxuuyasdhkjchukv'
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_KEY_PREFIX'] = 'session:'
app.config['PERMANENT_SESSION_LIFETIME'] = 7200
app.config['SESSION_REDIS'] = redis.Redis(host='localhost', port='6379', db=15)

f_session = Session()

f_session.init_app(app)



