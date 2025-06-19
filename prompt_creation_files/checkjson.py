import json

def validate_and_print_jsonl_line(file_path, line_to_print):
    required_keys = ["messages"]
    message_roles = {"system", "user", "assistant"}
    
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if line_number == line_to_print:
                try:
                    data = json.loads(line)
                    
                    # check for required keys
                    if not all(key in data for key in required_keys):
                        print(f"Line {line_number} is missing required keys.")
                        return
                    
                    messages = data["messages"]
                    
                    # to check message format
                    if not isinstance(messages, list) or len(messages) != 3:
                        print(f"Line {line_number} has incorrect 'messages' format or length.")
                        return
                    
                    for message in messages:
                        if "role" not in message or "content" not in message:
                            print(f"Line {line_number} is missing 'role' or 'content' in a message.")
                            return
                        if message["role"] not in message_roles:
                            print(f"Line {line_number} has an invalid role: {message['role']}.")
                            return
                    
                    # print content (readable) if it is valid
                    print(f"\nLine {line_number} is valid:\n")
                    for message in messages:
                        role = message["role"].capitalize()
                        content = message["content"]
                        print(f"{role}:\n{content}\n")
                    
                except json.JSONDecodeError as e:
                    print(f"Line {line_number} is invalid JSON: {e}")
                break

if __name__ == "__main__":
    file_path = "scores.jsonl"
    line_to_print = 3  # Change this to the line number you want to print
    validate_and_print_jsonl_line(file_path, line_to_print)
