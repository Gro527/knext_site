from flask import Flask


app = Flask('knext_site')
from knext_site.common import session
from knext_site.router import views