import fitz  # PyMuPDF
import re
from models import Brand, Model, Technical_Specifications, Engine, Transmission, Dimensions, Weight, Emission, Brake, Suspension, WheelTyreSize

def extract_data_from_pdf(pdf_path, db_session):
    document = fitz.open(pdf_path)
    text = ''
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    data = extract_data(text)
    if not data:
        return False

    # Extracted data
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
    manual_transmission = data.get('manual_transmission')
    automatic_transmission = data.get('automatic_transmission')
    length = data.get('length')
    width = data.get('width')
    height = data.get('height')
    wheel_base = data.get('wheel_base')
    turning_radius = data.get('turning_radius')
    ground_clearance = data.get('ground_clearance')
    fuel_tank_capacity = data.get('fuel_tank_capacity')
    boot_space = data.get('boot_space')
    seating_capacity = data.get('seating_capacity')
    kerb_weight = data.get('kerb_weight')
    gross_vehicle_weight = data.get('gross_vehicle_weight')
    emission_type = data.get('emission_type')
    front_brakes = data.get('front_brakes')
    rear_brakes = data.get('rear_brakes')
    front_suspension = data.get('front_suspension')
    rear_suspension = data.get('rear_suspension')
    tyre_size = data.get('tyre_size')

    # Add Brand
    brand = db_session.query(Brand).filter_by(brand_name=brand_name).first()
    if not brand:
        brand = Brand(brand_name=brand_name)
        db_session.add(brand)
        db_session.commit()

    # Add Model
    model = Model(model_name=model_name, brand_id=brand.brand_id, transmission_type=transmission_type, airbags=airbag_count, alloy_wheels=alloy_wheels)
    db_session.add(model)
    db_session.commit()

    # Add Technical Specifications
    technical_specifications = Technical_Specifications(variant="Default Variant",transmission_type=transmission_type,model_id=model.model_id)
    db_session.add(technical_specifications)
    db_session.commit()

    # Add Engine
    engine = Engine(engine_type=engine_type,engine_capacity=engine_capacity,max_power=max_power,max_torque=max_torque,number_of_cylinders=number_of_cylinders,fuel_efficiency=fuel_efficiency,idle_start_stop=idle_start_stop,model_id=model.model_id)
    db_session.add(engine)
    db_session.commit()

    # Add Transmission
    transmission = Transmission(manual=manual_transmission,automatic=automatic_transmission,model_id=model.model_id)
    db_session.add(transmission)
    db_session.commit()

    # Add Dimensions
    dimensions = Dimensions(length=length,width=width,height=height,wheel_base=wheel_base,turning_radius=turning_radius,ground_clearance=ground_clearance,fuel_tank_capacity=fuel_tank_capacity,boot_space=boot_space,seating_capacity=seating_capacity,model_id=model.model_id)
    db_session.add(dimensions)
    db_session.commit()

    # Add Weight
    weight = Weight(kerb_weight=kerb_weight,gross_vehicle_weight=gross_vehicle_weight,model_id=model.model_id)
    db_session.add(weight)
    db_session.commit()

    # Add Emission
    emission = Emission(emission_type=emission_type,model_id=model.model_id)
    db_session.add(emission)
    db_session.commit()

    # Add Brake
    brake = Brake(front_brakes=front_brakes,rear_brakes=rear_brakes,model_id=model.model_id)
    db_session.add(brake)
    db_session.commit()

    # Add Suspension
    suspension = Suspension(front_suspension=front_suspension,rear_suspension=rear_suspension,model_id=model.model_id)
    db_session.add(suspension)
    db_session.commit()

    # Add WheelTyreSize
    wheel_tyre_size = WheelTyreSize(tyre_size=tyre_size,model_id=model.model_id)
    db_session.add(wheel_tyre_size)
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
    manual_transmission = re.search(r'Manual Transmission:\s*(\w+)', text)
    automatic_transmission = re.search(r'Automatic Transmission:\s*(\w+)', text)
    length = re.search(r'Length:\s*(\d+)', text)
    width = re.search(r'Width:\s*(\d+)', text)
    height = re.search(r'Height:\s*(\d+)', text)
    wheel_base = re.search(r'Wheel Base:\s*(\d+)', text)
    turning_radius = re.search(r'Turning Radius:\s*([\d\.]+)', text)
    ground_clearance = re.search(r'Ground Clearance:\s*(\d+)', text)
    fuel_tank_capacity = re.search(r'Fuel Tank Capacity:\s*(\d+)', text)
    boot_space = re.search(r'Boot Space:\s*(\d+)', text)
    seating_capacity = re.search(r'Seating Capacity:\s*(\d+)', text)
    kerb_weight = re.search(r'Kerb Weight:\s*(\d+)', text)
    gross_vehicle_weight = re.search(r'Gross Vehicle Weight:\s*(\d+)', text)
    emission_type = re.search(r'Emission Type:\s*(\w+)', text)
    front_brakes = re.search(r'Front Brakes:\s*(\w+)', text)
    rear_brakes = re.search(r'Rear Brakes:\s*(\w+)', text)
    front_suspension = re.search(r'Front Suspension:\s*(\w+)', text)
    rear_suspension = re.search(r'Rear Suspension:\s*(\w+)', text)
    tyre_size = re.search(r'Tyre Size:\s*(\w+)', text)

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
    if manual_transmission:
        data['manual_transmission'] = manual_transmission.group(1)
    if automatic_transmission:
        data['automatic_transmission'] = automatic_transmission.group(1)
    if length:
        data['length'] = int(length.group(1))
    if width:
        data['width'] = int(width.group(1))
    if height:
        data['height'] = int(height.group(1))
    if wheel_base:
        data['wheel_base'] = int(wheel_base.group(1))
    if turning_radius:
        data['turning_radius'] = turning_radius.group(1)
    if ground_clearance:
        data['ground_clearance'] = int(ground_clearance.group(1))
    if fuel_tank_capacity:
        data['fuel_tank_capacity'] = int(fuel_tank_capacity.group(1))
    if boot_space:
        data['boot_space'] = int(boot_space.group(1))
    if seating_capacity:
        data['seating_capacity'] = int(seating_capacity.group(1))
    if kerb_weight:
        data['kerb_weight'] = int(kerb_weight.group(1))
    if gross_vehicle_weight:
        data['gross_vehicle_weight'] = int(gross_vehicle_weight.group(1))
    if emission_type:
        data['emission_type'] = emission_type.group(1)
    if front_brakes:
        data['front_brakes'] = front_brakes.group(1)
    if rear_brakes:
        data['rear_brakes'] = rear_brakes.group(1)
    if front_suspension:
        data['front_suspension'] = front_suspension.group(1)
    if rear_suspension:
        data['rear_suspension'] = rear_suspension.group(1)
    if tyre_size:
        data['tyre_size'] = tyre_size.group(1)

    return data
