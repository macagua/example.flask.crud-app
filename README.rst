==============
flask-crud-app
==============

Building a CRUD application with Flask and SQLAlchemy


Requeriments
============

Please execute the following commands:

::

    $ sudo apt-get install git python3-virtualenv python3-pip sqlitebrowser
    $ git clone https://github.com/macagua/flask-crud-app.git
    $ cd ./flask-crud-app
    $ virtualenv --python=/usr/bin/python3 venv
    $ source ./venv/bin/activate
    $ pip3 install -r requirements.txt


Running
=======

Please execute the following command:

::

    $ python3 bookmanager.py
     * Serving Flask app "bookmanager" (lazy loading)
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://0.0.0.0:8087/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 245-060-649
    127.0.0.1 - - [04/Jul/2019 14:21:17] "GET / HTTP/1.1" 200 -
    127.0.0.1 - - [04/Jul/2019 14:21:18] "GET /favicon.ico HTTP/1.1" 404 -


Open at your Web browser the following link http://127.0.0.1:8087


.. image:: https://raw.githubusercontent.com/macagua/flask-crud-app/master/docs/_static/bookmanager.png
   :class: image-inline


SQLAlchemy to SQL
=================


**db.session.commit()**::

    INSERT INTO book (title) VALUES ('The Hobbie');
    INSERT INTO book (title) VALUES ('The Lord of Rings');
    INSERT INTO book (title) VALUES ('The Silmarillion');
    INSERT INTO book (title) VALUES ('The Children of Húrin');
    COMMIT;

    UPDATE book
    SET title='The Lord of the Rings'
    WHERE title = 'The Lord of Rings';
    COMMIT;

**Book.query.all()**::

    SELECT * FROM book;

**Book.query.filter_by(title=oldtitle).first()**::

    SELECT book.title
    FROM book
    WHERE book.title = 'The Hobbie'
    LIMIT 1 OFFSET 0;

**db.session.delete(book)**::

    DELETE FROM book
    WHERE book.title = 'The Children of Húrin';


Reference
=========

- https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

- https://docs.sqlalchemy.org/en/latest/orm/tutorial.html

- http://flask-sqlalchemy.pocoo.org/2.3/queries/

