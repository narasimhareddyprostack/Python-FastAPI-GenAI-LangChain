import csv
import json
import os

INPUT_CSV = 'user.csv'
OUTPUT_JSON = 'emp.json'


def extract_csv(csv_path):
    """Read CSV data from the given path and return rows as a list."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    if not rows:
        raise ValueError(f"CSV file is empty: {csv_path}")

    return rows


def transform_rows(rows):
    """Transform CSV rows into a list of employee dictionaries."""
    header, *data_rows = rows
    transformed = []

    for index, row in enumerate(data_rows, start=2):
        if len(row) < 3:
            raise ValueError(f"Row {index} is missing required columns: {row}")

        transformed.append({
            'eid': row[0].strip(),
            'ename': row[1].strip(),
            'gender': row[2].strip()
        })

    return transformed


def load_json(data, json_path):
    """Write transformed data to a JSON file."""
    with open(json_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def run_etl(input_csv=INPUT_CSV, output_json=OUTPUT_JSON):
    """Run the full ETL process with error handling."""
    try:
        rows = extract_csv(input_csv)
        employee_data = transform_rows(rows)
        load_json(employee_data, output_json)
        print(f"New JSON file created successfully: {output_json}")
    except FileNotFoundError as err:
        print(f"ERROR: {err}")
    except ValueError as err:
        print(f"ERROR: {err}")
    except csv.Error as err:
        print(f"ERROR: Invalid CSV format: {err}")
    except json.JSONDecodeError as err:
        print(f"ERROR: Failed to write JSON: {err}")
    except Exception as err:
        print(f"UNEXPECTED ERROR: {err}")


if __name__ == '__main__':
    run_etl()