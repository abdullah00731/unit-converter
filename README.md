# Unit Converter

A command line tool that allows users to convert units across many categories.

Units and their convertion factors are defined in `units.json`

## Features

- convert between units using a common base unit
- 11 categories:
  - Length
  - Weight
  - area
  - volume
  - time
  - speed
  - pressure
  - power
  - data storage
  - frequency
  - angles
- input validation for categories, units and numbers (re-prompts for invalid inputs)
- easily add new categories or units by editing `units.json` file, not code change required

## Installation
1. clone/download repository
2. make sure `main.py` and `units.json` are in the same directory

## usage
run `main.py` from the command line

```bash
python main.py
```

Then:
1. pick a category
2. pick a unit to convert from
3. pick a unit to convert to
4. enter the value to convert

### Example
```
length
weight
area
...

please pick a category: Length

==== AVAILABLE UNITS ====
millimeters
centimeters
meters
kilometers
inches
feet
yards
miles

from: kilometers

To: meters

Value: 1

1.0 kilometers = 1000.0 meters
```

## How it works

Each category in `units.json` has a base unit and a set of units where each unit maps to a conversion factor relative to the base unit. To convert a value:
1. The value is multiplied by the "from" conversion factor to convert it to the base unit (`value * from_factor`)
2. The result is divided by the "to" conversion factor to convert it to the desired unit (`/ to_factor`)

`result = (value * from_factor) / to_factor`

## Adding new category
To add a new category add the following to the end of the `units.json` file:
```
"category_name": {
  "base_unit": "unit_name",
  "units": {
    "unit_one": "conversion_factor,
    "unit_two": convertion_factor,
    ...
}
}
```

> **Note** This converter uses a multiplicative factor relative to the base unit, making is suitable for categories such as length, weight, area, etc... but it is ***not*** suitable for categories such as temperature as they require an entire formula that includes addition/subtraction as well as a conversion factor
