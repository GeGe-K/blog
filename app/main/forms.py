from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    title = StringField('Comment title', validators = [Required()])
    comment = TextAreaField('comment')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators=[Required()])
    submit = SubmitField('Submit')

class AddPostForm(FlaskForm):
    title = StringField("Post Title", validators = [Required()])
    pitch = TextAreaField("Post", validators = [Required()])
   
    submit = SubmitField('Submit')

class Subscribe(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    submit = SubmitField('Submit')
