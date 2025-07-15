import os
import time
import csv
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

csv_filename = 'FinalTestFeed4096AllCriteriaResponse.csv'

output_filename = 'codellama-34b-Python-Test.csv'
progress_filename = 'codellama-34b-Python-Test.txt'
modelname = 'afrias5/codellama34b_finetuned'
basemodel = 'meta-llama/CodeLlama-34b-Python-hf'


def create_csv_if_not_exists(filename, headers):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headers)
        print(f"Created CSV file: {filename} with headers: {headers}")

def get_last_processed_row(filename):
    try:
        with open(filename, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        print(f"{filename} not found. Starting from row 0.")
        return 0

def save_last_processed_row(filename, row_number):
    with open(filename, 'w') as f:
        f.write(str(row_number))
    print(f"Saved last processed row: {row_number} to {filename}")

def count_csv_rows(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            return sum(1 for row in reader)
    except FileNotFoundError:
        return 0

def run_inference_and_save(csv_filename, output_filename, progress_filename):
    headers = ['instruction']

    create_csv_if_not_exists(output_filename, headers + ['response', 'inference_time'])

    last_processed_row = get_last_processed_row(progress_filename)

    config = PeftConfig.from_pretrained(modelname)

    base_model = AutoModelForCausalLM.from_pretrained(basemodel)
    tokenizer = AutoTokenizer.from_pretrained(modelname)

    base_model.resize_token_embeddings(len(tokenizer))

    model = PeftModel.from_pretrained(base_model, modelname)

    max_new_tokens = 2000  

    try:
        with open(csv_filename, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            print("Headers:", headers)
            instruction_index = headers.index('instruction')

            for current_row, row in enumerate(csv_reader, start=1):
                if current_row <= last_processed_row:
                    continue

                input_text = row[instruction_index].strip()

                if not input_text:
                    print(f"Empty row encountered at row {current_row}. Stopping.")
                    break

                print(f"Processing row {current_row}: {input_text}")

                inputs = tokenizer(input_text, return_tensors="pt")

                start_time = time.time()
                outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
                end_time = time.time()

                inference_time = end_time - start_time

                output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

                response_start = "###Response:"
                response_text = output_text.split(response_start, 1)[-1].strip() if response_start in output_text else output_text

                print(response_text)
                print(f"Inference time: {inference_time} seconds")

                with open(output_filename, mode='a', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(row + [response_text, inference_time])
                    print(f"Saved to {output_filename}: {row + [response_text, inference_time]}")

                save_last_processed_row(progress_filename, current_row)

    except Exception as e:
        print(f"Error reading the file: {e}")


run_inference_and_save(csv_filename, output_filename, progress_filename)
