import json
import os
import uuid
from flask import render_template, redirect, request, url_for, flash
from . import add
from .. import db
from ..models import Book
from .forms import AddbookForm
import fitz


@add.route("/addbook/", methods=["GET", "POST"])
def addbook():
    book_uuid = uuid.uuid4()
    form = AddbookForm()
    if request.method == "POST":
        book = request.files["book"]
        old_name = book.filename
        photo = request.files["photo"]
        bookDir = f"./app/static/books/{book_uuid}"
        flash(f"The book added {old_name}\nphoto{photo}")
        os.makedirs(bookDir)
        photo.save(os.path.join(bookDir, "cover.jpg"))
        book.save(os.path.join(bookDir, "book.pdf"))
        os.makedirs(bookDir + "/img")

        doc = fitz.open(os.path.join(bookDir, "book.pdf"))
        for pg in range(doc.pageCount):
            page = doc[pg]
            rotate = int(0)
            zoom_x = 2.0
            zoom_y = 2.0
            trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
            pm = page.get_pixmap(matrix=trans, alpha=False)
            pm.save(os.path.join(bookDir, "img/%s.png" % pg))

    if form.validate_on_submit():
        bookObj = Book(bookname=form.bookname.data, book_uuid=str(book_uuid),
                       summary=form.summary.data)
                       # summary=json.dumps(form.summary.raw_data))
        db.session.add(bookObj)
        db.session.commit()

        return redirect(url_for("add.addbook"))
    return render_template("add/addbook.html", form=form)
