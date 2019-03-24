# SNB_project/__init__.py
from flask import Flask

app = Flask(__name__)

from SNB_project.core.views import core
from SNB_project.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)
