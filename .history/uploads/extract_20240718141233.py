import fitz  # PyMuPDF
import re
from models import Brand, Model, Engine, Transmission, Dimensions, Weight, Emission, Brake, Suspension, WheelTyreSize

def extract_data_from_pdf(pdf_path, db_session):
    document = fitz.open(pdf_path)
    text = ''
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    data = extract_data(text)
    if not data:
        return False
    
    brand_name = data.get('brand_name')
    model_name = data.get('model_name')
    transmission_type = data.get('transmission_type')
    airbag_count = data.get('airbags')
    alloy_wheels = data.get('alloy_wheels')
    engine_type = data.get('engine_type')
    engine_capacity = data.get('engine_capacity')
    max_power = data.get('max_power')
    max_torque = data.get('max_torque')
    number_of_cylinders = data.get('number_of_cylinders')
    fuel_efficiency = data.get('fuel_efficiency')
    idle_start_stop = data.get('idle_start_stop')

    brand = db_session.query(Brand).filter_by(brand_name=brand_name).first()
    if not brand:
        brand = Brand(brand_name=brand_name)
        db_session.add(brand)
        db_session.commit()
    
    model = Model(model_name=model_name, brand_id=brand.brand_id, transmission_type=transmission_type, airbags=airbag_count, alloy_wheels=alloy_wheels)
    db_session.add(model)
    db_session.commit()
    
    engine = Engine(engine_type=engine_type, engine_capacity=engine_capacity, max_power=max_power, max_torque=max_torque, number_of_cylinders=number_of_cylinders, fuel_efficiency=fuel_efficiency, idle_start_stop=idle_start_stop, model_id=model.model_id)
    db_session.add(engine)
    db_session.commit()
    
    return True

def extract_data(text):
    data = {}
    brand_name = re.search(r'Brand:\s*(\w+)', text)
    model_name = re.search(r'Model:\s*(\w+)', text)
    transmission_type = re.search(r'Transmission:\s*(\w+)', text)
    airbag_count = re.search(r'Airbags:\s*(\d+)', text)
    alloy_wheels = re.search(r'Alloy Wheels:\s*(Yes|No)', text)
    engine_type = re.search(r'Engine Type:\s*(\w+)', text)
    engine_capacity = re.search(r'Engine Capacity:\s*(\d+)', text)
    max_power = re.search(r'Max Power:\s*([\d\.]+)', text)
    max_torque = re.search(r'Max Torque:\s*([\d\.]+)', text)
    number_of_cylinders = re.search(r'Number of Cylinders:\s*(\d+)', text)
    fuel_efficiency = re.search(r'Fuel Efficiency:\s*([\d\.]+)', text)
    idle_start_stop = re.search(r'Idle Start Stop:\s*(Yes|No)', text)

    if brand_name:
        data['brand_name'] = brand_name.group(1)
    if model_name:
        data['model_name'] = model_name.group(1)
    if transmission_type:
        data['transmission_type'] = transmission_type.group(1)
    if airbag_count:
        data['airbags'] = int(airbag_count.group(1))
    if alloy_wheels:
        data['alloy_wheels'] = True if alloy_wheels.group(1).lower() == 'yes' else False
    if engine_type:
        data['engine_type'] = engine_type.group(1)
    if engine_capacity:
        data['engine_capacity'] = int(engine_capacity.group(1))
    if max_power:
        data['max_power'] = max_power.group(1)
    if max_torque:
        data['max_torque'] = max_torque.group(1)
    if number_of_cylinders:
        data['number_of_cylinders'] = int(number_of_cylinders.group(1))
    if fuel_efficiency:
        data['fuel_efficiency'] = fuel_efficiency.group(1)
    if idle_start_stop:
        data['idle_start_stop'] = True if idle_start_stop.group(1).lower() == 'yes' else False
    
    return data
