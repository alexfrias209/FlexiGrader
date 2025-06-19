import pandas as pd
import json
import string
import re

def create_jsonl(description, criteria, main_code, external_files_info, detailed_feedback, scores):
    """Create JSONL formatted text with role-based messages."""
    system_content = """You are a diligent grading assistant for a Computer Science teacher. Your \
task is to read and analyze the Python code between <code> and </code> tags. Evaluate the \
code according to the criteria provided between <criteria> and </criteria> tags. Before \
evaluating, carefully review the CodeDescription provided between <description> and </description> tags \
to understand the purpose and context of the project. For each criterion, always assess the logic of \
the code, even if it does not run or contains errors, and provide both a score and detailed \
feedback explaining the reason for that score. After addressing all criteria, conclude by \
listing all individual scores in a summary. """

    
    if external_files_info.strip():
        user_content = f"""<description>\n{description}\n</description>\n\n{criteria}\n<Code>\n{main_code.strip()}\n</Code>\n\n{external_files_info.strip()}"""
    else:
        user_content = f"""<description>\n{description}\n</description>\n\n{criteria}\n<Code>\n{main_code.strip()}\n</Code>"""

    assistant_content = "\n\n".join(detailed_feedback) + f"\n\nReceived Score - {scores}"

    return {
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
    }

def get_external_files_code_and_name(row):
    """Extract code and names of external Python files from a CSV row.

    Args:
        row (pd.Series): A row from the CSV file.

    Returns:
        str: Formatted information about external Python files.
    """
    external_files_info = ""
    for i in range(1, 7):
        file_name = row.get(f"external_python_filename_{i}", None)
        file_code = row.get(f"external_python_filename_{i}_code", None)

        if pd.notna(file_name) and pd.notna(file_code):
            external_files_info += f"<Code>\n{clean_up_code(file_code.strip(), cleanup=True)}\n</Code>\n"

    return external_files_info.strip()

def clean_up_code(code, cleanup=True):
    """Clean up the provided code by removing non-printable characters and multiple '#' with a single '#'.

    Args:
        code (str): The code to be cleaned up.
        cleanup (bool): Flag indicating whether to clean up the code.

    Returns:
        str: The cleaned-up code.
    """
    # removing non-printable characters
    code = "".join(filter(lambda x: x in string.printable, code))

    if cleanup:
        # replace multiple '#' with a single '#', except when you got 8 '#'
        code = re.sub(r"(?<!#)#{2,7}(?!#)", "#", code)

    return code

def process_csv_to_jsonl(input_file, output_file):
    df = pd.read_csv(input_file, encoding="ISO-8859-1")
    jsonl_data = []

    for _, row in df.iterrows():
        description = row["ï»¿Description"]
        main_code = row["main_python_file_code"]
        external_files_info = get_external_files_code_and_name(row)
        detailed_feedback = [f"Criteria_{i}: {row[f'student_score_{i}']} out of {row[f'criteria{i}_total']}\nFeeback: {row[f'comments_{i}']}" for i in range(1, 7) if pd.notna(row[f'criteria{i}_description'])]
        scores = [row[f"student_score_{i}"] for i in range(1, 7) if pd.notna(row[f'criteria{i}_description'])]

        criteria_list = []
        for i in range(1, 7):
            crit_desc = row.get(f"criteria{i}_description", None)
            crit_rating = row.get(f"criteria{i}_rating", None)
            if pd.notna(crit_desc) and pd.notna(crit_rating):
                criteria_list.append(f"<criteria>\nCriteria_{i} description: {crit_desc}\n{crit_rating}\n</criteria>\n")
        criteria = "\n".join(criteria_list)
        
        jsonl_entry = create_jsonl(description, criteria, main_code, external_files_info, detailed_feedback, scores)
        jsonl_data.append(jsonl_entry)
    
    with open(output_file, 'w') as f:
        for entry in jsonl_data:
            f.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    input_file = "name.csv"
    output_file = "name.jsonl"
    process_csv_to_jsonl(input_file, output_file)
