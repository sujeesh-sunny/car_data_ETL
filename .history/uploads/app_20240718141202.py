from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from extract import extract_data_from_pdf
from models import db, Brand, Model, Engine, Transmission, Dimensions, Weight, Emission, Brake, Suspension, WheelTyreSize
from forms import UploadForm, SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost:3306/database_name'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        files = request.files.getlist('pdf_files')
        for file in files:
            if file:
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                success = extract_data_from_pdf(file_path, db.session)
                if success:
                    flash(f'{filename} successfully processed!', 'success')
                else:
                    flash(f'{filename} processing failed.', 'danger')
        return redirect(url_for('upload'))
    return render_template('upload.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        brand_name = form.brand_name.data
        transmission_type = form.transmission_type.data
        airbag_count = form.airbag_count.data
        alloy_wheels = form.alloy_wheels.data

        query = db.session.query(Model).join(Brand).filter(Brand.brand_name == brand_name)
        if transmission_type:
            query = query.filter(Model.transmission_type == transmission_type)
        if airbag_count is not None:
            query = query.filter(Model.airbags == airbag_count)
        if alloy_wheels:
            query = query.filter(Model.alloy_wheels == alloy_wheels)

        results = query.all()
    return render_template('search.html', form=form, results=results)

if __name__ == '__main__':
    app.run(debug=True)
