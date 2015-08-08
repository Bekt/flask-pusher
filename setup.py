"""
Flask-Pusher
------------

Flask-Pusher is a wrapper around `pusher-http-python` and
adds Pusher support for your Flask application.

Easy Setup
``````````

Quickstart:

.. code:: python

    from flask_pusher import Pusher

    app = Flask(__name__)
    pusher = Pusher(app)

    # Use any `pusher.Pusher` method.
    pusher.trigger('channel', 'my-event', {'data': 'It works!'})

Or using the factory pattern:

.. code:: python

    from flask_pusher import Pusher

    pusher = Pusher()

    def create_app():
        app = Flask(__name__):
        pusher.init_app(app)

        # Use any `pusher.Pusher` method.
        pusher.trigger('channel', 'my-event', {'data': 'It works!'})


Easy Installation
`````````````````

.. code:: bash

    $ pip install FlaskPusher
    $ # NOT Flask-Pusher

Links
`````

* `Source code and issues <https://github.com/Bekt/flask-pusher>`_
* `Documentation <http://flask-pusher.readthedocs.org/>`_
* `Official Pusher Python library <https://github.com/pusher/pusher-http-python>`_

"""
from setuptools import setup

setup(
    name='FlaskPusher',
    version='1.0',
    url='https://github.com/Bekt/flask-pusher',
    license='BSD',
    author='Kanat Bekt',
    author_email='bekt17+gh@gmail.com',
    description='Adds Pusher support for your Flask application.',
    long_description=__doc__,
    py_modules=['flask_pusher'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10',
        'pusher>=1.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    tests_require=['nose'],
    test_suite='flask_pusher_tests'
)
