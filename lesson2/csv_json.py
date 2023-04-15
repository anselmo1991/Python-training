import csv
import json
from pathlib import Path

csv_file = Path('C:/Users/Sofia_Shilova/Downloads/cars.csv')
json_file = Path('C:/Users/Sofia_Shilova/Downloads/cars.json')

with csv_file.open('r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
print(data)

with json_file.open('w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)