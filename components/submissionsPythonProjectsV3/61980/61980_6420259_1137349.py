import os
import PySimpleGUI as sg

def inspect_hw_files(folder_path):
    all_files = os.listdir(folder_path)
    
    non_conforming_files = []
    for file in all_files:
        file_name, file_ext = os.path.splitext(file)
        if (file_ext.lower() in ('.py')) and not (file_name.lower() == 'hw' or file_name.lower().startswith('hw_') or (file_name[2:].isdigit() and file_name.startswith('hw'))):
            non_conforming_files.append(file)
    if non_conforming_files:
        non_conforming_files.sort(key=str.lower)
        print(f'These files of Python in {folder_path} do not follow the hw naming:')
        for file in non_conforming_files:
            print(file)
    else:
        print(f'The following Python files in {folder_path} follow the correct formatting.')

schematic = [
    [sg.Text('Please select the folder you would like to check')],
    [sg.Input(key='_Folder_'), sg.FolderBrowse()],
    [sg.Button('Inspect Files'), sg.Button('Close window')],
]

tab = sg.Window('Inspect HW Files', schematic)

while True:
    event, data = tab.read()
    if event in (sg.WIN_CLOSED, 'Close window'):
        break
    elif event == 'Inspect Files':
        folder_path = data['_Folder_']
        if os.path.isdir(folder_path):
            inspect_hw_files(folder_path)
        else:
            print(f'An error has occurred in {folder_path}')

tab.close()