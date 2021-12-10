import os
from flask import render_template
from flask import abort
from . import main
from ..models import Book


@main.route("/index/")
@main.route("/")
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)


@main.route("/<book_id>")
def book(book_id):
    book = Book.query.filter_by(id=book_id).first()
    if book is None:
        abort(404)
    bookDir = f"./app/static/books/{book.book_uuid}/img/"
    tmp = os.listdir(bookDir)
    number_files = len(tmp)
    lst = []
    for i in range(number_files):
        lst.append(bookDir[6:] + str(i) + ".png")
    return render_template("book.html", book=book, number_files=number_files, lst=lst)
