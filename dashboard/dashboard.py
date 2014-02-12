import os
import sys
import imp
import glob
import importlib

from flask import Flask, request, session, g, redirect, url_for, abort, flash

import widgets

from views.dashboard import dashboard



widgets_path = os.path.join(os.path.dirname(__file__))
sys.path.append(widgets_path)

app = Flask(__name__)

app.config.from_object('dashboard.settings')
if os.environ.get('DASHBOARD_SETTINGS', None):
    app.config.from_envvar('DASHBOARD_SETTINGS')


if not 'widgets' in app.__dict__:
    setattr(app, 'widgets', {})


app.register_blueprint(dashboard, url_prefix="/")


for widget_name in app.config['WIDGETS']:
    name = "%s.%s.%s" % ('widgets', widget_name, widget_name)
    try:
        w = importlib.import_module(name, package=widgets)
        print "Loaded Widget: %s" % widget_name
    except ImportError:
        print "Unable to import %s" % name

