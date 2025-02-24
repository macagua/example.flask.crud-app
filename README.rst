======================
example.flask.crud-app
======================

.. image:: https://raw.githubusercontent.com/macagua/example.flask.crud-app/master/docs/_static/flask-vertical.png
   :class: image-inline

Building a CRUD application with Flask and SQLAlchemy


Requirements
============

Please execute the following commands:

::

    $ sudo apt install -y python3-dev python3-pip python3-virtualenv
    $ sudo apt install -y git
    $ sudo apt install -y sqlite3
    $ git clone https://github.com/macagua/example.flask.crud-app.git flask-crud-app
    $ cd ./flask-crud-app
    $ virtualenv --python /usr/bin/python3 venv
    $ source ./venv/bin/activate
    $ pip3 install -U pip
    $ pip3 install -r requirements.txt


----

Running
=======

Please execute the following command:

::

    $ python3 bookmanager.py
     * Serving Flask app 'bookmanager'
     * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
     * Running on all addresses (0.0.0.0)
     * Running on http://127.0.0.1:8087
     * Running on http://172.23.215.118:8087
    Press CTRL+C to quit
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 641-934-958
    127.0.0.1 - - [10/Feb/2025 14:10:06] "GET / HTTP/1.1" 200 -

Open at your Web browser the following link http://127.0.0.1:8087

.. image:: https://raw.githubusercontent.com/macagua/example.flask.crud-app/master/docs/_static/bookmanager.png
   :class: image-inline

Display a **Book Manager** app, like the previous figure.


----

SQLAlchemy to SQL
=================

The following code is an example of how SQLAlchemy translates
the Python code to SQL code.

**db.session.commit()**

Insert the following books into the database:

::


    INSERT INTO book (title) VALUES ('The Hobbie');
    INSERT INTO book (title) VALUES ('The Lord of Rings');
    INSERT INTO book (title) VALUES ('The Silmarillion');
    INSERT INTO book (title) VALUES ('The Children of Húrin');
    COMMIT;

----

Update the title of the book 'The Lord of Rings' to 'The Lord of the Rings':

::


    UPDATE book
    SET title='The Lord of the Rings'
    WHERE title = 'The Lord of Rings';
    COMMIT;

----

**Book.query.all()**

Search for all books:

::


    SELECT * FROM book;

**Book.query.filter_by(title=old_title).first()**:

Search for the book with the title 'The Hobbie':

::


    SELECT book.title
    FROM book
    WHERE book.title = 'The Hobbie'
    LIMIT 1 OFFSET 0;

----

**db.session.delete(book)**:

Delete the book with the title 'The Children of Húrin':

::


    DELETE FROM book
    WHERE book.title = 'The Children of Húrin';


References
==========

- `Building a CRUD application with Flask and SQLAlchemy <https://www.codementor.io/@garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2>`_.
- `SQLAlchemy Unified Tutorial <https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial>`_.
- `Modifying and Querying Data — Flask-SQLAlchemy Documentation <https://flask-sqlalchemy.palletsprojects.com/en/stable/queries/>`_.
