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
        response = input(prompt).lower()
        if response == 'y':
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
        # bank_flip = get_yes_no_input(f"Should bank {bank_index} be flipped? (y/n): ")
        
        cylinder_count = get_int_input(f"Enter the number of cylinders in bank {bank_index}: ")
        for i in range(cylinder_count):
            bank_cylinders.append(get_int_input(f"Enter cylinder {i} number: "))
            firing_order.append(bank_cylinders[-1])
        
        bank_angle = get_float_input(f"Enter the bank angle for bank {bank_index} (degrees): ")
        
        banks.append(engine_generator.Bank(bank_cylinders, bank_angle))
        # banks[-1].flip = bank_flip
    
    engine = engine_generator.Engine(banks, firing_order)
    engine.engine_name = engine_name
    
    # engine.starter_torque = get_float_input("Enter starter torque: ")
    # engine.starter_speed = get_float_input("Enter starter speed: ")
    # engine.redline = get_float_input("Enter redline RPM: ")
    # engine.throttle_gamma = get_float_input("Enter throttle gamma: ")
    
    # engine.crank_mass = get_float_input("Enter crank mass: ")
    # engine.bore = get_float_input("Enter bore: ")
    # engine.stroke = get_float_input("Enter stroke: ")
    # engine.rod_length = get_float_input("Enter rod length: ")
    # engine.compression_height = get_float_input("Enter compression height: ")
    
    engine.generate()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(script_directory, "engines")

    create_folder_if_not_exists(output_folder)

    output_filename = os.path.join(output_folder, f"{engine_name.lower()}_engine.mr")

    engine.write_to_file(output_filename)

    print(f"Engine configuration '{engine_name}' generated and saved to '{output_filename}'.")

if __name__ == "__main__":
    generate_engine()