import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = "sqlite:///{}".format(
    os.path.join(
        PROJECT_DIR,
        "book_database.sqlite3"
    )
)

app = Flask(__name__, static_folder='static')
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_FILE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class Base(DeclarativeBase):
    """DeclarativeBase is a class that is used to create
    a new base class for declarative class definitions.

    Args:
        DeclarativeBase (class): A class that is used to create
    """
    pass

# SQLAlchemy is an ORM (Object Relational Mapper) that allows
# you to interact with databases using Python objects.
db = SQLAlchemy(app, model_class=Base)


class Book(db.Model):
    """Book model

    Args:
        db (class): An instance of SQLAlchemy

    Returns:
        class: A class that represents a book model
    """
    id: Mapped[int] = mapped_column(
        db.Integer,
        primary_key=True
    )
    title: Mapped[str] = mapped_column(
        db.String(80),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return "<Title: {}>".format(self.title)

@app.route("/", methods=["GET", "POST"])
def home():
    """Home page route"""
    books = None
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    # Get all books
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/update", methods=["POST"])
def update():
    """Update book title route"""
    try:
        new_title = request.form.get("new_title")
        old_title = request.form.get("old_title")
        book = Book.query.filter_by(title=old_title).first()
        book.title = new_title
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    """Delete book route"""
    title = request.form.get("title")
    book = Book.query.filter_by(title=title).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

with app.app_context():
    # Create tables
    db.create_all()
    # Run the app
    app.run(host='0.0.0.0', port=8087, debug=True)
