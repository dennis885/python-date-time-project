calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute(num_of_days_element):
    if num_of_days_element.isdigit():
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0. Please enter a positive number.")
    else:
        print("Your input is not a valid number. Please enter a valid number.")

user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of days and conversion unit!\n")
    if user_input == "exit":
        break
    for num_of_days_element in set(user_input.split(":")):
        validate_and_execute()
