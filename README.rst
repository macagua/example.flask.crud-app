==============
flask-crud-app
==============

Building a CRUD application with Flask and SQLAlchemy

Requeriments
=============

Please execute the following commands:

::

    sudo apt-get install sqlitebrowser
    git clone https://github.com/macagua/flask-crud-app.git
    virtualenv --python=/usr/bin/python3 .
    source bin/activate
    pip3 install -r requirements.txt

Running
========

Please execute the following command:

::


    python3 bookmanager.py


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

