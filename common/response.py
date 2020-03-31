import datetime
from flask.json import JSONEncoder
from flask import jsonify



def _try_to_serialize(data):
    if isinstance(data, (list, tuple)):
        return [_try_to_serialize(m) for m in data]

    serial_func = getattr(data, 'serialize', None)
    if serial_func and callable(serial_func):
        return data.serialize()
    else:
        return data

def ok(data={}, **kwargs):
    response = {
        'status': 0,
        'message': 'ok',
        'data': _try_to_serialize(data)
    }
    response.update(kwargs)
    return jsonify(response)


def error(message='error', status=-1, data={}, **kwargs):
    response = {
        'status': status,
        'message': message,
        'data': _try_to_serialize(data)
    }

    response.update(kwargs)

    return jsonify(response)


class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        try:
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
