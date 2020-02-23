from flask import session
import functools

print session

def require_login(function):
    @functools.wraps(function)
    def warp(*args, **kwargs):
        pass