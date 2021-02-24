from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import *
from Game import Game
from wtforms.compat import string_types, text_type
from wtforms.validators import Required


class LoginForm(FlaskForm):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[DataRequired()])
    game_id = StringField('Game room', validators=[Optional()])
    submit = SubmitField('Play')

    def validate_game_id(form, field):
        if not field.data:
            field.data = 1
        elif not int(field.data) in [1, 2, 3, 4]: # TODO in future check list of existing gamerooms
            raise ValidationError("The room does not exist")


class NewGameForm(FlaskForm):
    values = []
    for o in range(Game.minGuessingTime + Game.timeStep, Game.maxGuessingTime, Game.timeStep):
        values.append(o)

    name = StringField('Name', validators=[DataRequired()])
    waiting_time = SelectField(u'Waiting Time', choices=values)
    submit = SubmitField('Create game')

