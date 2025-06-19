import pandas as pd
import json
import string
import re

def create_jsonl(description, criteria, main_code, external_files_info, detailed_feedback, scores, detailed_scores):
    """Create JSONL formatted text with role-based messages."""
    system_content = """You are a diligent grading assistant for a Computer Science teacher. Given the code and a set of criteria with scores, you will: 
1. Read the code between <code> and </code> tags. 
2. Read each criterion between <criteria> and </criteria> tags. 
3. Read the scores provided between <scores> and </scores> (matching each criterion). 
4. Provide a short explanation ("Feedback") for why each criterion received its score.
5. Output your final response in the format shown between <format> and </format> tags.

<format>
Repeat for each criterion in ascending order (1, 2, 3, ...):

Criteria_{'i'}: {'score_i'} out of {'max_score_i'}
Feedback: {'explanation_for_criterion_i'}

*After listing all criteria feedback, conclude with one line showing the final scores \
as a list in the order the criteria were presented.*

Received Score - [{'score_1'}, {'score_2'}, ..., {'score_n'}]
</format>"""

    # Conditional addition of newlines based on external_files_info
    if external_files_info.strip():
        user_content = f"""### CodeDescription: {description}\n\n{criteria}\n### MainPythonFileCode\n<code>\n{main_code.strip()}\n</code>\n\n{external_files_info.strip()}\n{"<score>\n" + "".join(detailed_scores) + "</score>"}"""
    else:
        user_content = f"""### CodeDescription: {description}\n\n{criteria}\n### MainPythonFileCode\n<code>\n{main_code.strip()}\n</code>\n{"<score>\n" + "".join(detailed_scores) + "</score>"}"""

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
            external_files_info += f"### ExternalPythonFile - {file_name} code:\n<code>\n{clean_up_code(file_code.strip(), cleanup=True)}\n</code>\n"

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
        description = row["Description"]
        main_code = row["main_python_file_code"]
        external_files_info = get_external_files_code_and_name(row)
        detailed_feedback = [f"Criteria_{i}: {row[f'student_score_{i}']} out of {row[f'criteria{i}_total']}\nFeeback: {row[f'comments_{i}']}" for i in range(1, 9) if pd.notna(row[f'criteria{i}_description'])]
        detailed_scores = [f"Criteria_{i}: {row[f'student_score_{i}']} out of {row[f'criteria{i}_total']}\n" for i in range(1, 9) if pd.notna(row[f'criteria{i}_description'])]
        scores = [row[f"student_score_{i}"] for i in range(1, 9) if pd.notna(row[f'criteria{i}_description'])]

        criteria_list = []
        for i in range(1, 9):
            crit_desc = row.get(f"criteria{i}_description", None)
            crit_rating = row.get(f"criteria{i}_rating", None)
            if pd.notna(crit_desc) and pd.notna(crit_rating):
                criteria_list.append(f"<criteria>\n### Criteria_{i}:\nDescription: {crit_desc}\n{crit_rating}\n</criteria>\n")
        criteria = "\n".join(criteria_list)
        
        jsonl_entry = create_jsonl(description, criteria, main_code, external_files_info, detailed_feedback, scores, detailed_scores)
        jsonl_data.append(jsonl_entry)
    
    with open(output_file, 'w') as f:
        for entry in jsonl_data:
            f.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    input_file = "FinalUpdatedData.csv"
    output_file = "ScoreExplanation.jsonl"
    process_csv_to_jsonl(input_file, output_file)
