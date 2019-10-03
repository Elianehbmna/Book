from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField,ValidationError,RadioField,FileField
from wtforms.validators import Required,Email,EqualTo
from flask_wtf.file import FileField
from ..models import User

class BookForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    summary = TextAreaField("Book summary ?",validators=[Required()])
    category = RadioField('Label', choices=[ ('Educational','Educational'), ('Musical','Musical'),('Religion','Religion'),('Comedy','Comedy')],validators=[Required()])
    poster= FileField(validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()
class UpvoteForm(FlaskForm):
	submit = SubmitField()

class ContactForm(FlaskForm):
   Email = StringField('Enter Your Email', validators=[Required()])
   description = TextAreaField('Leave a message',validators=[Required()])
   submit = SubmitField()




