import json

FILENAME = "units.json"


def load_json(fileName):
    try:
        with open(fileName, "r") as file:
            units = json.load(file)

            return units
    except FileNotFoundError:
        print("ERROR - file not found")
        quit()


def float_input(prompt):
    while True:
        try:
            num = float(input(prompt))
        except ValueError:
            print("invalid number - please try again")
            continue

        break

    return num


def print_json(toPrint):
    print(json.dumps(toPrint, indent=4))


def convert(category, convert_from, convert_to, value):
    category_details = data[category]["units"]

    from_factor = category_details[convert_from]
    to_factor = category_details[convert_to]

    # convert value to base unit then convert the base unit to the desired unit
    # value * from_factor -> convert to base unit
    # / to_factor -> convert to desired unit
    result = (value * from_factor) / to_factor

    return result


data = load_json(FILENAME)

categories = list(data)
for i in categories:
    print(i)

category = input("\nPlease pick a category: ")
while True:
    if category not in categories:
        category = input("invalid category - please try again: ")
        continue

    break

category_units = data[category]["units"]

print("\n==== AVAILABLE UNITS ====")

for i in list(category_units):
    print(i)

convert_from = input("\nFrom: ")
while True:
    if convert_from not in category_units:
        convert_from = input("invalid unit - please try again: ")
        continue

    break

convert_to = input("\nTo: ")
while True:
    if convert_to not in category_units:
        convert_to = input("invalid unit - please try again: ")
        continue

    break

value = float_input("\nValue: ")

result = convert(category, convert_from, convert_to, value)

print(f"\n{value:,} {convert_from} = {round(result, 5):,} {convert_to}")
