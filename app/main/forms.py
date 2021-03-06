from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,FileField,SubmitField
from wtforms.validators import Required,Email,EqualTo

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators = [Required()])
    comment = TextAreaField('Comment')
    name = StringField('Name', validators= [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')

class AddPostForm(FlaskForm):
    title = StringField("Post Title", validators = [Required()])
    content = TextAreaField("Post", validators = [Required()])
    photo = FileField('Select an image', validators=[Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    name = StringField('Enter your name', validators=[Required])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Submit')
