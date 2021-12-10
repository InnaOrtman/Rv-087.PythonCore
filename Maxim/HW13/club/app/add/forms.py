from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class AddbookForm(FlaskForm):
    bookname = StringField("Enter the name of the book",
                           validators=[DataRequired(), Length(1, 128)])
    book = FileField("Choose book in PDF format",
                     validators=[DataRequired()])
    photo = FileField("Choose the cover of book",
                      validators=[DataRequired()])
    summary = TextAreaField("Enter annotation of the book",
                            validators=[DataRequired(), Length(1, 2000)],
                            render_kw={"rows": 20})
    submit = SubmitField("Upload")
