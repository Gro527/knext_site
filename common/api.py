from flask import session, request
from flask import make_response
from flask import jsonify
import functools


def require_login(function):
    @functools.wraps(function)
    def warp(*args, **kwargs):
        if session.get(request.cookies.get('session_id')) == None:
            resp = make_response(
                jsonify(status=-1, message='Please login first!')
            )
            resp.status_code = 401
            return resp
        else:
            return function(*args, **kwargs)
    
    return warp

            