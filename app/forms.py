from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, HiddenField
from wtforms.validators import ValidationError, DataRequired, Length


class PostForm(FlaskForm):
    post = TextAreaField(
        'Paste a link and say something about it',
        validators=[DataRequired(), Length(min=1, max=3000)])
    embed_tag = HiddenField()
    preview_url = HiddenField()
    preview_title = HiddenField()
    preview_description = HiddenField()
    preview_image = HiddenField()
    submit = SubmitField('Post')
