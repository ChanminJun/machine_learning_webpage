# SNB_project/__init__.py
from flask import Flask

app = Flask(__name__)

from SNB_project.core.views import core
app.register_blueprint(core)
