from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Brand(db.Model):
    __tablename__ = 'Brand'
    brand_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(255), nullable=False)
    models = db.relationship('Model', backref='brand', lazy=True)

class Model(db.Model):
    __tablename__ = 'Model'
    model_id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(255), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('Brand.brand_id'), nullable=False)
    transmission_type = db.Column(db.String(255))
    airbags = db.Column(db.Integer)
    alloy_wheels = db.Column(db.Boolean)
    engine = db.relationship('Engine', backref='model', lazy=True)
    transmission = db.relationship('Transmission', backref='model', lazy=True)
    dimensions = db.relationship('Dimensions', backref='model', lazy=True)
    weight = db.relationship('Weight', backref='model', lazy=True)
    emission = db.relationship('Emission', backref='model', lazy=True)
    brake = db.relationship('Brake', backref='model', lazy=True)
    suspension = db.relationship('Suspension', backref='model', lazy=True)
    wheel_tyre = db.relationship('WheelTyreSize', backref='model', lazy=True)

class Engine(db.Model):
    __tablename__ = 'Engine'
    engine_id = db.Column(db.Integer, primary_key=True)
    engine_type = db.Column(db.String(255))
    engine_capacity = db.Column(db.Integer)
    max_power = db.Column(db.String(255))
    max_torque = db.Column(db.String(255))
    number_of_cylinders = db.Column(db.Integer)
    fuel_efficiency = db.Column(db.String(255))
    idle_start_stop = db.Column(db.Boolean)
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class Transmission(db.Model):
    __tablename__ = 'Transmission'
    transmission_id = db.Column(db.Integer, primary_key=True)
    manual = db.Column(db.String(255))
    automatic = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class Dimensions(db.Model):
    __tablename__ = 'Dimensions'
    dimension_id = db.Column(db.Integer, primary_key=True)
    length = db.Column(db.Integer)
    width = db.Column(db.Integer)
    height = db.Column(db.Integer)
    wheel_base = db.Column(db.Integer)
    turning_radius = db.Column(db.Float)
    ground_clearance = db.Column(db.Integer)
    fuel_tank_capacity = db.Column(db.Integer)
    boot_space = db.Column(db.Integer)
    seating_capacity = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class Weight(db.Model):
    __tablename__ = 'Weight'
    weight_id = db.Column(db.Integer, primary_key=True)
    kerb_weight = db.Column(db.Integer)
    gross_vehicle_weight = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class Emission(db.Model):
    __tablename__ = 'Emission'
    emission_id = db.Column(db.Integer, primary_key=True)
    emission_type = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class Brake(db.Model):
    __tablename__ = 'Brake'
    brake_id = db.Column(db.Integer, primary_key=True)
    front_brakes = db.Column(db.String(255))
    rear_brakes = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class Suspension(db.Model):
    __tablename__ = 'Suspension'
    suspension_id = db.Column(db.Integer, primary_key=True)
    front_suspension = db.Column(db.String(255))
    rear_suspension = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)

class WheelTyreSize(db.Model):
    __tablename__ = 'Wheel_Tyre_Size'
    wheel_tyre_id = db.Column(db.Integer, primary_key=True)
    tyre_size = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('Model.model_id'), nullable=False)
