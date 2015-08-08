# -*- coding: utf-8 -*-
"""Tests for `flask_pusher.py`."""

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from flask import Flask

from flask_pusher import Pusher


class FlaskPusherTest(unittest.TestCase):

    configs = {
        'PUSHER_APP_ID': '123',
        'PUSHER_KEY': 'abc',
        'PUSHER_SECRET': 'secret',
        'PUSHER_PORT': 20
    }

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config.update(self.configs)

    def test_init_no_app(self):
        pusher = Pusher()
        self.assertRaises(AttributeError, lambda: getattr(pusher, 'app_id'))

    def test_init(self):
        pusher = Pusher(self.app)
        self._assert_init(pusher)

    def test_json_encoder(self):
        pusher = Pusher(self.app)
        self.assertEqual(pusher._json_encoder, self.app.json_encoder)

    def test_init_app(self):
        pusher = Pusher()
        pusher.init_app(self.app)
        self._assert_init(pusher)

    def test_options(self):
        pusher = Pusher()
        pusher.init_app(self.app, host='eu', timeout=20)
        self.assertEqual(pusher.host, 'eu')
        self.assertEqual(pusher.timeout, 20)

    def test_override_config(self):
        pusher = Pusher()
        pusher.init_app(self.app, port=1337)
        self.assertEqual(pusher.port, 1337)

    def _assert_init(self, pusher):
        for k in [('app_id', 'PUSHER_APP_ID'),
                  ('key', 'PUSHER_KEY'),
                  ('secret', 'PUSHER_SECRET'),
                  ('port', 'PUSHER_PORT')]:
            self.assertEqual(getattr(pusher, k[0]), self.app.config[k[1]])
