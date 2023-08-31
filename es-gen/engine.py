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
            cylinder_number = get_int_input(f"Enter cylinder {i} number (starts at 0): ")
            bank_cylinders.append(cylinder_number)
            firing_order.append(cylinder_number) 

        bank_angle_input = input(f"Enter the angle of bank {bank_index} (0 anti-clockwise): ")
        bank_angle = float(bank_angle_input) if bank_angle_input else 0

        bank_flip = get_yes_no_input(f"Should bank {bank_index} be flipped? (y/N): ")

        banks.append(engine_generator.Bank(bank_cylinders, bank_angle))
        banks[-1].flip = bank_flip
    
    modified_firing_order = []

    modify_firing_order = get_yes_no_input(f"Do you want to modify the firing order? (y/N): ")
    if modify_firing_order:
        for cylinder_number in firing_order:
            new_cylinder_order = get_int_input(f"Enter firing order for cylinder {cylinder_number} (starts at 1): ")
            modified_firing_order.append(new_cylinder_order - 1)
    else:
        modified_firing_order = list(range(len(firing_order)))

    engine = engine_generator.Engine(banks, modified_firing_order)
    engine.engine_name = engine_name

    engine.generate()

    use_advanced_settings = get_yes_no_input("Do you want to configure advanced settings? (y/N): ")
    if use_advanced_settings:
        starter_torque_input = input("Enter starter torque (70): ")
        engine.starter_torque = int(starter_torque_input) if starter_torque_input else 70

        starter_speed_input = input("Enter starter speed (50): ")
        engine.starter_speed = int(starter_speed_input) if starter_speed_input else 500

        redline_input = input("Enter redline (8000): ")
        engine.redline = int(redline_input) if redline_input else 8000

        rev_limit_input = input(f"Enter rev limit ({engine.redline + 1000}): ")
        engine.rev_limit = int(rev_limit_input) if rev_limit_input else engine.redline + 1000
             
        limiter_duration_input = input("Enter limiter duration (0.1): ")
        engine.limiter_duration = int(limiter_duration_input) if limiter_duration_input else 0.1
            
        #

        stroke_input = input("Enter stroke (86): ")
        engine.stroke = int(stroke_input) if stroke_input else 86
            
        bore_input = input("Enter bore (86): ")
        engine.bore = int(bore_input) if bore_input else 86
            
        rod_length_input = input("Enter rod length (120): ")
        engine.rod_length = int(rod_length_input) if rod_length_input else 120

        rod_mass_input = input("Enter rod mass (50): ")
        engine.rod_mass = int(rod_mass_input) if rod_mass_input else 50
            
        compression_height_input = input("Enter compression height (25.4): ")
        engine.compression_height = int(compression_height_input) if compression_height_input else 25.4
            
        crank_mass_input = input("Enter crank mass (10): ")
        engine.crank_mass = int(crank_mass_input) if crank_mass_input else 10

        flywheel_mass_input = input("Enter flywheel mass (10): ")
        engine.flywheel_mass = int(flywheel_mass_input) if flywheel_mass_input else 10
            
        flywheel_radius_input = input("Enter flywheel radius (100): ")
        engine.flywheel_radius = int(flywheel_radius_input) if flywheel_radius_input else 100
            
        piston_mass_input = input("Enter piston mass (50): ")
        engine.piston_mass = int(piston_mass_input) if piston_mass_input else 50
            
        #

        lobe_separation_input = input("Enter lobe separation (114): ")
        engine.lobe_separation = int(lobe_separation_input) if lobe_separation_input else 114
            
        camshaft_base_radius_input = input("Enter camshaft base radius (0.5): ")
        engine.camshaft_base_radius = int(camshaft_base_radius_input) if camshaft_base_radius_input else 0.5

        lobe_center_input = input("Enter lobe_center (90): ")
        engine.intake_lobe_center = int(lobe_center_input) if lobe_center_input else 90
        engine.exhaust_lobe_center = int(lobe_center_input) if lobe_center_input else 90

        lobe_lift_input = input("Enter lobe lift (551): ")
        engine.intake_lobe_lift = int(lobe_lift_input) if lobe_lift_input else 551
        engine.exhaust_lobe_lift = int(lobe_lift_input) if lobe_lift_input else 551
            
        lobe_duration_input = input("Enter lobe duration (235): ")
        engine.intake_lobe_duration = int(lobe_duration_input) if lobe_duration_input else 235
        engine.exhaust_lobe_duration = int(lobe_duration_input) if lobe_duration_input else 235
            
        lobe_steps_input = input("Enter lobe steps (512): ")
        engine.intake_lobe_steps = int(lobe_steps_input) if lobe_steps_input else 512
        engine.exhaust_lobe_steps = int(lobe_steps_input) if lobe_steps_input else 512
            
        #

        exhaust_length_input = input("Enter exhaust length (20): ")
        engine.exhaust_length = int(exhaust_length_input) if exhaust_length_input else 20
            
        idle_throttle_plate_position_input = input("Enter idle throttle plate position (0.999): ")
        engine.idle_throttle_plate_position = int(idle_throttle_plate_position_input) if idle_throttle_plate_position_input else 0.999

    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_directory, "engines")

    create_folder_if_not_exists(output_folder)

    output_filename = os.path.join(output_folder, f"{engine_name.lower()}_engine.mr")
    engine.write_to_file(output_filename)

    print(f"Engine configuration '{engine_name}' generated and saved to '{output_filename}'.")

if __name__ == "__main__":
    generate_engine()