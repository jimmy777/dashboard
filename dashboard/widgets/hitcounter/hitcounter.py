"""
    Example Widget:

        @widget.register(name="hitcounter", template_name='hitcounter.html')
        def hitcounter(data):
            return data

        NOTES:
            - template_name is optional and will default to <name>.html if not provided.
            - data is the data you want to be sent to the dashboard template to parse and
              display
            - Flow: POST to api -> look for id in POST data -> delegate to registered widget with id -> widget returns parsed json -> dashboard template is rendered and js deals with data via SSE subscribption and event
"""

from dashboard.helpers import widget

@widget.register(name="hitcounter")
def hitcounter(data):
    print "hi from hitcounter"
    return data
