Welcome to Flask-Pusher's documentation!
========================================

**Flask-Pusher** is a wrapper around `pusher-http-python <https://github.com/pusher/pusher-http-python>`_ 
that adds `Pusher <https://pusher.com/>`_ support for your Flask application.

Requirements
------------

    Flask>=0.10
    pusher>=1.1

Installation
------------

    $ pip install Flask-Pusher

Quickstart
----------

The following snippet shows how to add Flask-Pusher to a Flask application.

    from flask_pusher import Pusher

    app = Flask(__name__)
    pusher = Pusher(app)

    # Use any `pusher.Pusher` method.
    pusher.trigger('channel', 'my-event', {'data': 'It works!'})


The factory pattern via the `init_app` method is also supported.
The following snippet demonstrates this style.

    from flask_pusher import Pusher

    pusher = Pusher()

    def create_app():
        app = Flask(__name__):
        pusher.init_app(app)


Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

