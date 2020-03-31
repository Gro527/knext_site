# coding: utf-8
from knext_site.router import app
from flask import session, request, make_response
from knext_site.common import log_in, response,api
from knext_site.lib.knext_rpc_client import ExtractionClient
from knext_site.db.models import User
import time

API_PREFIX = '/api/v1'
client = ExtractionClient()


@app.route('/')
def home():
    '''
    for test usage
    '''
    return response.ok('welcome to knext site')


@app.route(API_PREFIX + '/signup', methods=['post'])
def signup():
    input_json = request.get_json()
    username = input_json.get('username')
    password = input_json.get('password')
    try:
        user = User.get_by_username(username)
        if user:
            return response.error('user already exists')
        user = User(input_json)
        user.save()
        session[user.username] = {'status': 0}
        resp = make_response(response.ok())
        resp.set_cookie('session_id', user.username)
        return resp
    except:
        return response.error('server error, please contact admin')


@app.route(API_PREFIX + '/login', methods=['post'])
def login():
    input_json = request.get_json()
    username = input_json.get('username')
    password = input_json.get('password')
    user = User.login(username, password)
    if not user:
        return response.error('invalid username or password')
    cookie = request.cookies.get('session')
    session[cookie] = {'username': user.username}
    resp = make_response(response.ok())
    return resp


@app.route(API_PREFIX + '/extract', methods=['post'])
@api.require_login
def extract():
    input_json = request.get_json()
    text = input_json.get('text')
    print text
    res = client.get_extraction(text.encode('utf-8'), 'knext_site')
    print res
    return response.ok(res)






