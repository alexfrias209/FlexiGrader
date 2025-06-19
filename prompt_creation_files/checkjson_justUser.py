import json

def view_user_content(jsonl_file, entry_number):
    """
    View the 'content' field of the 'user' role for a specific entry in the JSONL file.
    
    Args:
        jsonl_file (str): Path to the JSONL file.
        entry_number (int): The entry number to view (1-based index).
    """
    try:
        with open(jsonl_file, 'r') as f:
            for current_index, line in enumerate(f, start=1):
                if current_index == entry_number:
                    # Parse the JSON for the specified entry
                    entry = json.loads(line)
                    
                    # Extract and print the "user" content
                    for message in entry.get("messages", []):
                        if message["role"] == "user":
                            print(f"Entry {entry_number} - User Content:\n")
                            print(message["content"])
                            return
                    print(f"No 'user' role found in Entry {entry_number}.")
                    return
        
        print(f"Entry {entry_number} does not exist in the file.")
    except FileNotFoundError:
        print(f"Error: The file '{jsonl_file}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON content in the file '{jsonl_file}'.")

if __name__ == "__main__":
    # Path to the JSONL file
    jsonl_file = "FeedFinal4096V10.jsonl"
    
    # Specify the entry number you want to view (126 in this case)
    entry_number = 2
    
    view_user_content(jsonl_file, entry_number)
