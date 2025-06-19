import csv
import os

base_directory = 'Projects_Version_2/Projects_Version_2'

csv_data = []


for folder_name in os.listdir(base_directory):
    folder_path = os.path.join(base_directory, folder_name)
    
    if not os.path.isdir(folder_path):
        continue  
    
    python_files = []
    
    for file in os.listdir(folder_path):
        if file.endswith('.py'):
            file_path = os.path.join(folder_path, file)
            python_files.append(file)
    
    python_files.sort()
    

    row = [folder_name] + [item for pair in zip(python_files, [''] * len(python_files)) for item in pair]
    
    row.extend([''] * (24 - len(row)))
    
    csv_data.append(row[:24])  

headers = ['folder_name', 'main_python_file_name', 'main_python_file_code']
for i in range(1, 7):  
    headers.extend([f'external_python_filename_{i}', f'external_python_filename_{i}_code'])

csv_file_path = 'python_file_names_by_folder.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(csv_data)

print(f"CSV file created at: {csv_file_path}")
