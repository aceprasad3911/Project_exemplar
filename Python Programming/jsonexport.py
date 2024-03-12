# option 4
import csv
import json
from datahandler import data


# export using department name
def export(departmentid):
    depp = []
    reader = csv.DictReader(data)
    department_rec = [row for row in reader if row['Department'].lower() == departmentid.lower()]
    depp.append(department_rec)
    output_file_path = f'{departmentid}_data.json'
    with open(output_file_path, 'w') as json_file:
        json.dump(department_rec, json_file, indent=2)
