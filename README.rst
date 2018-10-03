==============
flask-crud-app
==============

Building a CRUD application with Flask and SQLAlchemy


Requeriments
============

Please execute the following commands:

::

    sudo apt-get install sqlitebrowser
    git clone https://github.com/macagua/flask-crud-app.git
    virtualenv --python=/usr/bin/python3 venv
    source ./venv/bin/activate
    pip3 install -r requirements.txt


Running
=======

Please execute the following command:

::


    python3 bookmanager.py


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
