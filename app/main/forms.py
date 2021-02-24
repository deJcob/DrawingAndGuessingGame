from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import *
from wtforms.compat import string_types, text_type
from wtforms.validators import Required


class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[DataRequired()])
    game_id = StringField('game_id', validators=[Optional()])
    submit = SubmitField('Play')

    def validate_game_id(form, field):
        if not field.data:
            field.data = 1
        elif not int(field.data) in [1, 2, 3, 4]: # TODO in future check list of existing gamerooms
            raise ValidationError("The room does not exist")
