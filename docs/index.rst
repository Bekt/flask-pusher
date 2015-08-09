Welcome to Flask-Pusher's documentation!
========================================

**Flask-Pusher** is a wrapper around `pusher-http-python <https://github.com/pusher/pusher-http-python>`_ 
that adds `Pusher <https://pusher.com/>`_ support for your Flask application.

Installation
------------
::

    $ pip install FlaskPusher
    $ # NOT Flask-Pusher

The extension has been tested with ``Flask>=0.10`` and ``pusher>=1.1``.

Quickstart
----------

The following snippet shows how to add Flask-Pusher to a Flask application.
::

    from flask_pusher import Pusher

    app = Flask(__name__)
    pusher = Pusher(app)

    # Use any `pusher.Pusher` method.
    pusher.trigger('channel', 'my-event', {'data': 'It works!'})


The factory pattern via the ``init_app()`` method is also supported.
The following snippet demonstrates this style.
::

    from flask_pusher import Pusher

    pusher = Pusher()

    def create_app():
        app = Flask(__name__)
        pusher.init_app(app)

        # Use any `pusher.Pusher` method.
        pusher.trigger('channel', 'my-event', {'data': 'It works!'})


Configuration
-------------

You can choose to provide Pusher options through your Flask application configs.
At the minimum, it is recommended you provide ``PUSHER_APP_ID``, ``PUSHER_KEY``,
and ``PUSHER_SECRET``. However, you can provide these and other options during
``Pusher`` instantiation. See the next section.

===================  =================
Option               Corresponding Arg
===================  =================
PUSHER_APP_ID        ``app_id``
PUSHER_KEY           ``key``
PUSHER_SECRET        ``secret``
PUSHER_SSL           ``ssl``
PUSHER_HOST          ``host``
PUSHER_PORT          ``port``
PUSHER_CLUSTER       ``cluster``
PUSHER_BACKEND       ``backend``
PUSHER_TIMEOUT       ``timeout``
PUSHER_JSON_ENCODER  ``json_encoder``
PUSHER_JSON_DECODER  ``json_decoder``
===================  =================

For the description of the corresponding arguments, please refer to the
``pusher-http-python`` `documentation <https://github.com/pusher/pusher-http-python>`_.


Providing Options During Instantiation
--------------------------------------

You can also provide zero or more options as keyword arguments,
just as you would provide them for ``pusher-http-python``.
The options provided as keyword arguments take precedence over the options
provided in the application configs.
::

    from flask_pusher import Pusher

    app = Flask(__name__)
    pusher = Pusher(app, secret='top-secret', ssl=False)

Works with ``init_app()`` style as well:
::
    from pusher.tornade import TornadoBackend
    from flask_pusher import Pusher

    pusher = Pusher()
    ...
    pusher.init_app(app, secret='1337', cluster='eu',
                    backend=TornadoBackend)


API Reference
-------------

This documentation is automatically generated from the source code.

.. module:: flask_pusher

.. autoclass:: Pusher
   :members:

