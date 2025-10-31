# Factorio Item Calculator

A simple script to calculate required intermediate items and raw resources for Factorio item production.

## Features

- **Item Calculation**: The script calculates the required intermediate items and raw resources needed for production in Factorio.
- **Item Consumption List**: It generates a detailed list of item consumption based on the defined recipes.
- **File Input**: The program reads item data from a JSON file, allowing for easy updates and modifications.

## Supported Resources

- Intermediate items
- Raw resources
- Custom items defined in `items.json`

## Project Files

- `factorio_obj.py`: Contains the `factorioItem` class and functions to read items from a file and calculate item consumption and production lists.
- `Factory.py`: Main script that initializes the item list from `items.json` and defines resource outputs.
- `items.json`: JSON file containing item data used by the scripts.
- `obsolete.py`: Contains deprecated code or functions that are no longer in use.
- `LICENSE`: The license file for the project.

## Usage

To use the scripts, ensure that `items.json` is present in the same directory and run `Factory.py` to calculate item requirements.

## Functions

### ReadItemsFromFile(file_name: str)
This function reads item data from a specified JSON file and initializes the item list.

### getItemConsumptionList(il: dict[str, factorioItem])
This function calculates the consumption list for items based on the provided item list.

### printItemConsumptionList(icl: dict[str, float])
This function prints the item consumption list in a readable format.

