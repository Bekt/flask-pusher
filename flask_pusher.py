# -*- coding: utf-8 -*-
from pusher import Pusher as BasePusher


class Pusher(BasePusher):

    def __init__(self, app=None, **options):
        if app is not None:
            self.init_app(app, **options)

    def init_app(self, app, **options):
        """Configures the application."""
        sd = lambda k, v: options.setdefault(k, v)
        conf = app.config

        sd('app_id', conf.get('PUSHER_APP_ID'))
        sd('key', conf.get('PUSHER_KEY'))
        sd('secret', conf.get('PUSHER_SECRET'))
        sd('ssl', conf.get('PUSHER_SSL', True))
        sd('host', conf.get('PUSHER_HOST'))
        sd('port', conf.get('PUSHER_PORT'))
        sd('cluster', conf.get('PUSHER_CLUSTER'))
        sd('backend', conf.get('PUSHER_BACKEND'))
        sd('json_encoder', (conf.get('PUSHER_JSON_ENCODER')
                            or app.json_encoder))
        sd('json_decoder', (conf.get('PUSHER_JSON_DECODER')
                            or app.json_decoder))
        if conf.get('PUSHER_TIMEOUT'):
            sd('timeout', conf.get('PUSHER_TIMEOUT'))

        super(Pusher, self).__init__(**options)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['pusher'] = self
