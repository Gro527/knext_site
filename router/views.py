from knext_site.router import app
from flask import session, request
from knext_site.common import log_in
import time

API_PREFIX = '/api/v1'


@app.route('/')
def home():
    '''
    for test usage
    '''
    print 'aaa'
    print session
    session['guhaoping'] = time.time()
    return 'success'


@app.route('/get')
def get_session():
    return str(session['guhaoping'])
    

@app.route(API_PREFIX + '/login', methods=['post'])
def login():
    input_json = request.get_json()
    username = input_json.get(username)
    password = input_json.get(password)



