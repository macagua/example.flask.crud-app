==============
flask-crud-app
==============

Building a CRUD application with Flask and SQLAlchemy

Requeriments
=============

Please execute the following commands:

::

    sudo apt-get install sqlitebrowser
    virtualenv --python=/usr/bin/python3 .
    source Flask_1_0_2/bin/activate
    pip3 install -r requirements.txt
    pip freeze > requirements.txt
    mkdir -p ~/python/flask-crud-app/templates
    cd ~/python/flask-crud-app
    python bookmanager.py


Initializing database
=====================

From the IPython execute the following commands:

::

    ipython3
    >>> from bookmanager import db
    >>> db.create_all()
    >>> exit()

Reference
=========

- https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

