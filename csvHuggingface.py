import csv
from datasets import Dataset, load_dataset
from huggingface_hub import HfApi, HfFolder

# set you csv path
csv_file_path = 'name.csv'

# this will be your huggingface dataset name
dataset_name = 'name'

# set HF_TOKEN, easier if you just add to bashrc
api = HfApi()
token = HfFolder.get_token()
    
dataset = load_dataset('csv', data_files={'train': csv_file_path})
    
dataset.push_to_hub(dataset_name)



