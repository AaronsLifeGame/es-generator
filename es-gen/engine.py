import os
import engine_generator

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if not response:
            return False
        elif response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def generate_engine():
    engine_name = input("Enter the engine name: ")
    bank_count = get_int_input("Enter the number of banks: ")

    banks = []
    firing_order = []

    for bank_index in range(bank_count):
        bank_cylinders = []

        cylinder_count = get_int_input(f"Enter the number of cylinders in bank {bank_index}: ")
        for i in range(cylinder_count):
            while True:
                cylinder_number = get_int_input(f"Enter cylinder {i} number (starts at 0): ")
                if cylinder_number not in firing_order:
                    bank_cylinders.append(cylinder_number)
                    firing_order.append(cylinder_number)
                    break
                else:
                    print(f"Cylinder {cylinder_number} is already in use. Please enter a different cylinder number.")

        bank_angle_input = input(f"Enter the angle of bank {bank_index} [0 anti-clockwise]: ")
        bank_angle = float(bank_angle_input) if bank_angle_input else 0

        bank_flip = get_yes_no_input(f"Should bank {bank_index} be flipped? [y/N]: ")

        banks.append(engine_generator.Bank(bank_cylinders, bank_angle))
        banks[-1].flip = bank_flip
    
    modified_firing_order = []

    modify_firing_order = get_yes_no_input(f"Do you want to modify the firing order? [y/N]: ")
    if modify_firing_order:
        for cylinder_number in firing_order:
            new_cylinder_order = get_int_input(f"Enter firing order for cylinder {cylinder_number} (starts at 1): ")
            modified_firing_order.append(new_cylinder_order - 1)
    else:
        modified_firing_order = list(range(len(firing_order)))

    engine = engine_generator.Engine(banks, modified_firing_order)
    engine.engine_name = engine_name

    engine.generate()

    modify_engine = get_yes_no_input("Do you want to modify the engine settings? [y/N]: ")
    if modify_engine:
        starter_torque_input = input("Enter starter torque [70 lb_ft]: ")
        engine.starter_torque = float(starter_torque_input) if starter_torque_input else 70.0

        starter_speed_input = input("Enter starter speed [50 rpm]: ")
        engine.starter_speed = float(starter_speed_input) if starter_speed_input else 500.0

        redline_input = input("Enter redline [8000 rpm]: ")
        engine.redline = float(redline_input) if redline_input else 8000.0

        rev_limit_input = input(f"Enter rev limit [{engine.redline + 1000} rpm]: ")
        engine.rev_limit = float(rev_limit_input) if rev_limit_input else engine.redline + 1000.0

        limiter_duration_input = input("Enter limiter duration [0.1]: ")
        engine.limiter_duration = float(limiter_duration_input) if limiter_duration_input else 0.1

        #

        stroke_input = input("Enter stroke [86 mm]: ")
        engine.stroke = float(stroke_input) if stroke_input else 86.0

        bore_input = input("Enter bore [86 mm]: ")
        engine.bore = float(bore_input) if bore_input else 86.0

        rod_length_input = input("Enter rod length [120 mm]: ")
        engine.rod_length = float(rod_length_input) if rod_length_input else 120.0

        rod_mass_input = input("Enter rod mass [50 g]: ")
        engine.rod_mass = float(rod_mass_input) if rod_mass_input else 50.0

        compression_height_input = input("Enter compression height [25.4 mm]: ")
        engine.compression_height = float(compression_height_input) if compression_height_input else 25.4

        crank_mass_input = input("Enter crank mass [10 kg]: ")
        engine.crank_mass = float(crank_mass_input) if crank_mass_input else 10.0

        flywheel_mass_input = input("Enter flywheel mass [10 kg]: ")
        engine.flywheel_mass = float(flywheel_mass_input) if flywheel_mass_input else 10.0

        flywheel_radius_input = input("Enter flywheel radius [100 mm]: ")
        engine.flywheel_radius = float(flywheel_radius_input) if flywheel_radius_input else 100.0

        piston_mass_input = input("Enter piston mass [50 g]: ")
        engine.piston_mass = float(piston_mass_input) if piston_mass_input else 50.0

        #

        lobe_separation_input = input("Enter lobe separation [114 deg]: ")
        engine.lobe_separation = float(lobe_separation_input) if lobe_separation_input else 114.0

        camshaft_base_radius_input = input("Enter camshaft base radius [0.5 inch]: ")
        engine.camshaft_base_radius = float(camshaft_base_radius_input) if camshaft_base_radius_input else 0.5

        lobe_center_input = input("Enter lobe center [90 deg]: ")
        engine.intake_lobe_center = float(lobe_center_input) if lobe_center_input else 90.0
        engine.exhaust_lobe_center = float(lobe_center_input) if lobe_center_input else 90.0

        lobe_lift_input = input("Enter lobe lift [551 thou]: ")
        engine.intake_lobe_lift = float(lobe_lift_input) if lobe_lift_input else 551.0
        engine.exhaust_lobe_lift = float(lobe_lift_input) if lobe_lift_input else 551.0

        lobe_duration_input = input("Enter lobe duration [235 deg]: ")
        engine.intake_lobe_duration = float(lobe_duration_input) if lobe_duration_input else 235.0
        engine.exhaust_lobe_duration = float(lobe_duration_input) if lobe_duration_input else 235.0

        lobe_steps_input = input("Enter lobe steps [512]: ")
        engine.intake_lobe_steps = int(lobe_steps_input) if lobe_steps_input else 512
        engine.exhaust_lobe_steps = int(lobe_steps_input) if lobe_steps_input else 512

        
        chamber_volume_input = input("Enter chamber volume [100 cc]: ")
        engine.chamber_volume = int(chamber_volume_input) if chamber_volume_input else 100

        #

        exhaust_length_input = input("Enter exhaust length [20 inch]: ")
        engine.exhaust_length = float(exhaust_length_input) if exhaust_length_input else 20.0

        idle_throttle_plate_position_input = input("Enter idle throttle plate position [0.999]: ")
        engine.idle_throttle_plate_position = float(idle_throttle_plate_position_input) if idle_throttle_plate_position_input else 0.999

    modify_transmission = get_yes_no_input("Do you want to modify the transmission settings? [y/N]: ")
    if modify_transmission:
        max_clutch_torque_input = input("Enter max clutch torque [1000 lb_ft]: ")
        engine.transmission.max_clutch_torque = float(max_clutch_torque_input) if max_clutch_torque_input else 1000
        
        modify_gears = get_yes_no_input("Do you want to modify the gear ratios? [y/N]: ")
        if modify_gears:
            gear_count = get_int_input("Enter the number of gears [2.8, 2.29, 1.93, 1.583, 1.375, 1.19]: ")
            gear_ratios = []
            for i in range(gear_count):
                gear_ratio_input = input(f"Enter gear ratio for gear {i + 1}: ")
                gear_ratio = float(gear_ratio_input) if gear_ratio_input else 1.0
                gear_ratios.append(gear_ratio)
            engine.transmission.gears = gear_ratios

    modify_vehicle = get_yes_no_input("Do you want to modify the vehicle settings? [y/N]: ")
    if modify_vehicle:
        mass_input = input("Enter vehicle mass [798 kg]: ")
        engine.vehicle.mass = float(mass_input) if mass_input else 798
        
        drag_coefficient_input = input("Enter drag coefficient [0.9]: ")
        engine.vehicle.drag_coefficient = float(drag_coefficient_input) if drag_coefficient_input else 0.9
        
        front_area_input = input("Enter front cross-sectional area [72 inch]: ")
        rear_area_input = input("Enter rear cross-sectional area [36 inch]: ")
        engine.vehicle.cross_sectional_area = [
            float(front_area_input) if front_area_input else 72, 
            float(rear_area_input) if rear_area_input else 36
        ]
        
        diff_ratio_input = input("Enter diff ratio [4.10]: ")
        engine.vehicle.diff_ratio = float(diff_ratio_input) if diff_ratio_input else 4.10
        
        tire_radius_input = input("Enter tire radius [9 inch]: ")
        engine.vehicle.tire_radius = float(tire_radius_input) if tire_radius_input else 9
        
        rolling_resistance_input = input("Enter rolling resistance [200 N]: ")
        engine.vehicle.rolling_resistance = float(rolling_resistance_input) if rolling_resistance_input else 200

    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_directory, "engines")

    create_folder_if_not_exists(output_folder)

    output_filename = os.path.join(output_folder, f"{engine_name.lower()}.mr")
    engine.write_to_file(output_filename)

    print(f"Engine configuration '{engine_name}' generated and saved to '{output_filename}'.")

if __name__ == "__main__":
    generate_engine()