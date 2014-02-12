import sys
import os

from dashboard.dashboard import app
import inspect


def register(**kwargs):

    def register_widget(f):
        name = kwargs.get('name', str(f.__name__))
        template = kwargs.get('template_name', name+'.html')

        path = os.path.dirname(sys.modules[f.__module__].__file__)

        tmplpath = os.path.join(path, template)
        if not os.path.exists(tmplpath):
            print 'Missing Template File: ' + tmplpath
            raise ImportError

        app.widgets[name] = {}
        app.widgets[name]['f'] = f
        app.widgets[name]['template'] = template
        app.widgets[name]['path'] = path

        return f

    return register_widget

