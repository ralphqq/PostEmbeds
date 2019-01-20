from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Length


class PostForm(FlaskForm):
    post = TextAreaField(
        'What are you thinking about?',
        validators=[DataRequired(), Length(min=1, max=500)])
    embed_tag = HiddenField()
    submit = SubmitField('Post')
