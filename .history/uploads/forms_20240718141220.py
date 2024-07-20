from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, FileField, SubmitField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    pdf_files = FileField('Upload PDF Files', validators=[DataRequired()])
    submit = SubmitField('Upload')

class SearchForm(FlaskForm):
    brand_name = StringField('Brand Name', validators=[DataRequired()])
    transmission_type = StringField('Transmission Type')
    airbag_count = IntegerField('Number of Airbags')
    alloy_wheels = BooleanField('Alloy Wheels')
    submit = SubmitField('Search')
