import json
import os
import logging

logging.basicConfig(
    filename='Json_error',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s')

folder_path = '../Task 2'

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                json.load(file)
            except json.JSONDecodeError as e:
                logging.error(f'Invalid JSON in file {filename}: {e}')
