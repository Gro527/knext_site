import logging
import sys
from knext_site.router import app
from flask import session
from flask_session import Session
from knext_site.db import mappers
import redis



if __name__ == '__main__':
    if len(sys.argv) == 2:
        port = sys.argv[1]
    else:
        port = 5555
    app.run(host='0.0.0.0', port=port, debug= True)

