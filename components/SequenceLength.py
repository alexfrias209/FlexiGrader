import pandas as pd
from transformers import AutoTokenizer

csv_file = "name.csv"
dataset = pd.read_csv(csv_file)

tokenizer = AutoTokenizer.from_pretrained("afrias5/codellama34b_finetuned")

print(f"{'Row':<6}{'Text Length':<12}")

max_length = 0
max_row = -1
long_texts = []
token_lengths = []

for idx, row in dataset.iterrows():
    text = row["instruction"]  
    text_tokens = tokenizer(text, return_tensors="pt")["input_ids"].shape[1]
    token_lengths.append(text_tokens)

    if text_tokens > max_length:
        max_length = text_tokens
        max_row = idx

    print(f"{idx + 2:<6}{text_tokens:<12}") 

    if text_tokens > 4096:
        long_texts.append((idx, text_tokens))

print(f"\nMaximum token length: {max_length} at row {max_row + 2}")  

if long_texts:
    print("\nRows with text length > 4096:")
    for idx, token_length in long_texts:
        print(f"Row {idx + 2}: {token_length} tokens")  
else:
    print("\nNo rows with text length > 4096.")

print("\nInteractive Mode: Type a row number to view its text (up to 500 characters), or type 'exit' to quit.")
while True:
    user_input = input("Enter row number or 'exit': ").strip()

    if user_input.lower() == "exit":
        print("Exiting...")
        break
    elif user_input.isdigit():
        row_number = int(user_input)
        if row_number >= 2 and row_number < len(dataset) + 2:
            dataset_index = row_number - 2 
            token_length = token_lengths[dataset_index]
            text = dataset.iloc[dataset_index]["instruction"][:4000]  
            print(f"\nRow {row_number} (Token Length: {token_length}):")
            print(f"{text}\n")
        else:
            print("Invalid row number. Please try again.")
    else:
        print("Invalid input. Please enter a row number or 'exit'.")
