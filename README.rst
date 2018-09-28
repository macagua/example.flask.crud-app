==============
flask-crud-app
==============


Requeriments
=============

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

::
  ipython3
  >>> from bookmanager import db
  >>> db.create_all()
  >>> exit()


