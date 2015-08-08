# Flask-Pusher

![](http://flask-pusher.readthedocs.org/en/latest/_static/logo.jpg)

**Flask-Pusher** is a wrapper around the official Pusher Python library 
[pusher-http-python](https://github.com/pusher/pusher-http-python) that
adds [Pusher](https://pusher.com/) support for a Flask application.

This extension lets you access all the methods in `pusher-http-python`
while still giving you the flexibility on how to configure and
instantiate the Pusher instance in a Flask-style.

The Pusher instance's JSON encoder and decoder also fallback to the `app.json_encoder` and
`app.json_decoder` if they are not specified.

* [Documentation](http://flask-pusher.readthedocs.org/en/latest/)
* [Official Pusher Python
  library](https://github.com/pusher/pusher-http-python)


## Installation

```bash
$ pip install FlaskPusher
$ # NOT Flask-Pusher
```

The extension has been tested with `Flask>=0.10` and `pusher>=1.1`.

## Quickstart

The following snippet shows how to add Flask-Pusher to a Flask application.

```python
from flask_pusher import Pusher

app = Flask(__name__)
pusher = Pusher(app)

# Use any pusher.Pusher method.
pusher.trigger('channel', 'my-event', {'data': 'It works!'})
```

Or using the factory pattern:

```python
from flask_pusher import Pusher

pusher = Pusher()

def create_app():
    app = Flask(__name__):
    pusher.init_app(app)

    # Use any pusher.Pusher method.
    pusher.trigger('channel', 'my-event', {'data': 'It works!'})
```

## Configuration
In your Flask application configs, you can specify the following options.
You can choose to provide zero or more of these options. 

Option | Corresponding Argument
-------| :--------------------:
PUSHER_APP_ID | `app_id`
PUSHER_KEY | `key`
PUSHER_SECRET | `secret`
PUSHER_SSL | `ssl`
PUSHER_HOST | `host`
PUSHER_PORT | `port`
PUSHER_CLUSTER | `cluster`
PUSHER_BACKEND | `backend`
PUSHER_JSON_ENCODER | `json_encoder`
PUSHER_JSON_DECODER | `json_decoder`
PUSHER_TIMEOUT | `timeout`

For the description of the corresponding arguments, please refer to the
[pusher-http-python](https://github.com/pusher/pusher-http-python)
documentation.

## Providing Options During Instantiation

You can also provide zero or more options as keyword arguments, just as
you would provide them for `pusher-http-python`.

```python
from flask_pusher import Pusher

app = Flask(__name__)
pusher = Pusher(app, secret='top-secret', ssl=False)
```

Works with `init_app()` style as well:

```python
from pusher.tornade import TornadoBackend
from flask_pusher import Pusher

pusher = Pusher()
...
pusher.init_app(app, cluster='eu', backend=TornadoBackend)
```

## Tests

You can run the tests with: `python setup.py test`

## License

Simplified BSD. See LICENSE.md for details.
