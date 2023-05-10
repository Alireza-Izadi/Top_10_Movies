from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

class EditForm(FlaskForm):
     rating = FloatField("Rating", validators=[DataRequired()])
     review = StringField("Review", validators=[DataRequired()])
     submit = SubmitField("Edit")

class AddMovie(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    year = IntegerField("Year", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    rating = FloatField("Rating", validators=[DataRequired()])
    ranking = IntegerField("Ranking", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    img_url = StringField("Image Url", validators=[DataRequired()])
    submit = SubmitField('Submit')
