import pandas as pd
import argparse
import re
import string


def alpaca_columns(
    description, criteria, main_code, external_files_info, detailed_feedback, scores
):
    """Get components to make alpaca style dataset.

    Args:
        description (str): A brief description of the python project.
        criteria (str): The criteria used for grading the code.
        main_code (str): The main Python code to be graded.
        external_files_info (str): external python file name and code combined as a string together.
        detailed_feedback (list of str): Formatted string of criteria, score, and max score combined
        scores (list of int): Student scores for each criteria.

    Returns:
        tuple: A tuple containing the instruction, an empty placeholder for input column,\
             the output, and the combined text.
    """
    instruction = create_instruction(description, criteria, main_code, external_files_info)
    outputs = create_outputs(detailed_feedback, scores)
    text = f"{instruction}\n{outputs}"
    return instruction, "", outputs, text


def create_instruction(description, criteria, main_code, external_files_info):
    """Generate an instruction text based on the provided details.

    Args:
        description (str): A brief description of the python project.
        criteria (str): The criteria used for grading the code.
        main_code (str): The main Python code to be graded.
        external_files_info (str): external python file name and code combined as a string together.

    Returns:
        str: The formatted prompt for instruction column.
    """
    return f"""\
### Instruction: You are a diligent grading assistant for a Computer Science teacher. Your \
task is to read and analyze the Python code between <code> and </code> tags. Evaluate the \
code according to the criteria provided between <criteria> and </criteria> tags. Before \
evaluating, carefully review the CodeDescription provided between <description> and </description> tags \
to understand the purpose and context of the project. For each criterion, always assess \
the logic of the code even if it does not run or contains \
errors, and provide a score. After addressing all criteria, \
conclude by listing all the individual scores in a summary. 

### CodeDescription: 
<description>
{description}
</description>

{criteria}

### MainPythonFileCode\n<code>\n{main_code}\n</code>
{external_files_info}\
"""


def info_from_csv(row, index, cleanup):
    """Extract information from the CSV row.

    Args:
        row (pd.Series): A row from the CSV file.
        index (int): The index of the row.
        cleanup (bool): Flag indicating whether to remove consecutive #'s.

    Returns:
        tuple: A tuple containing description, criteria, main code,\
        external files (name and code combined as string),
        feedback (string of criteria, score, and max score combined), and student scores.
    """
    description = row["ï»¿Description"]
    external_files_info = get_external_files_code_and_name(row)
    criteria, scores, detailed_feedback = get_criteria_feedback_scores(row, index)
    main_code = row["main_python_file_code"]
    description, criteria, main_code, external_files_info, detailed_feedback = formatting(
        description, criteria, main_code, external_files_info, detailed_feedback, cleanup
    )
    return description, criteria, main_code, external_files_info, detailed_feedback, scores


def create_outputs(detailed_feedback, scores):
    """Create output text from detailed feedback and scores.

    Args:
        detailed_feedback (list of str): Formatted string of criteria, score, and max score combined
        scores (list of int): Student scores for each criteria.

    Returns:
        str: The formatted output text column.
    """
    return "### Response:\n" + "\n".join(detailed_feedback) + f"\nReceived Score - {scores}"


def formatting(description, criteria, main_code, external_files_info, detailed_feedback, cleanup):
    """Formatting and cleaning up code some more.

    Args:
        description (str): A brief description of the python project.
        criteria (str): The criteria used for grading the code.
        main_code (str): The main Python code to be graded.
        external_files_info (str): External python file name and code combined as a string together.
        detailed_feedback (list of str): Formatted string of criteria, score, and max score combined.
        cleanup (bool): Flag indicating whether to clean up the code.

    Returns:
        tuple: A tuple containing formatted description, criteria, main code, external files info, and detailed feedback.
    """
    description = clean_up_code(description.strip(), cleanup=False)
    criteria = clean_up_code(criteria.strip(), cleanup=False)
    main_code = clean_up_code(main_code.strip(), cleanup=True)
    external_files_info = clean_up_code(external_files_info.strip(), cleanup=False)
    detailed_feedback = [
        clean_up_code(feedback.strip() + "\n", cleanup=False) for feedback in detailed_feedback
    ]

    if external_files_info:
        external_files_info = "\n" + external_files_info + "\n"

    return description, criteria, main_code, external_files_info, detailed_feedback


def clean_up_code(code, cleanup=True):
    """Clean up the provided code by removing non-printable characters and multiple '#' with a single '#'.

    Args:
        code (str): The code to be cleaned up.
        cleanup (bool): Flag indicating whether to clean up the code.

    Returns:
        str: The cleaned-up code.
    """
    # removing non-printable characters was causing issues
    code = "".join(filter(lambda x: x in string.printable, code))

    if cleanup:
        # replace multiple '#' with a single '#', except when you got 8 '#'
        code = re.sub(r"(?<!#)#{2,7}(?!#)", "#", code)

    return code


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
            external_files_info += f"### ExternalPythonFile - {file_name} code:\n<code>\n{clean_up_code(file_code.strip(),cleanup=True)}\n</code>\n\n"

    return external_files_info


def get_criteria_feedback_scores(row, index):
    """Extract criteria, feedback, and scores from a CSV row.

    Args:
        row (pd.Series): A row from the CSV file.
        index (int): The index of the row.

    Returns:
        tuple: A tuple containing criteria, scores, and \
        feedback (string of criteria, score, and max score combined).
    """
    criteria = ""
    scores = []
    detailed_feedback = []

    for j in range(1, 9):
        crit_desc = row.get(f"criteria{j}_description", None)
        crit_rating = row.get(f"criteria{j}_rating", None)
        max_score = row.get(f"criteria{j}_total", None)
        score = row.get(f"student_score_{j}", None)
        feedback = row.get(f"comments_{j}", None)

        if pd.notna(crit_desc) and pd.notna(crit_rating):
            criteria += f"### Criteria_{j}:\n<criteria>\nDescription: {crit_desc}\n{crit_rating}\n</criteria>\n\n"

        if pd.notna(score):
            try:
                score = int(score)
                max_score = int(max_score)
                scores.append(score)
                detailed_feedback.append(
                    f"Criteria_{j}: {score} out of {max_score}\n"
                )
            except ValueError:
                print(f"Error processing score for criteria {j} in row {index}: {score}")

    return criteria, scores, detailed_feedback


def save_first_instruction_to_file(df, filename, encoding="utf-8"):
    """Save the first instruction to a text file.

    Args:
        df (pd.DataFrame): DataFrame containing instructions.
        filename (str): Name of the file to save the instruction.
        encoding (str, optional): Encoding of the file. Defaults to 'utf-8'.
    """
    with open(filename, "w", encoding=encoding) as file:
        first_instruction = df.loc[0, "instruction"]
        if isinstance(first_instruction, pd.Series):
            first_instruction = first_instruction.iloc[0]
        file.write(first_instruction)


def save_to_csv(df, output_file):
    """Save the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
        output_file (str): Name of the output CSV file.
    """
    df.to_csv(output_file, index=False)


def main(input_file, output_file, textfile="default.txt", save=False, row_number=3, cleanup=True):
    """Main function to process CSV and generate instructions and outputs.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to the output CSV file.
        textfile (str, optional): File to save the first instruction. Defaults to "default.txt".
        save (bool, optional): Flag to save the DataFrame to a CSV file. Defaults to False.
        row_number (int, optional): Row number to print sample generated text. Defaults to 3.
        cleanup (bool, optional): Flag to clean up the code. Defaults to True.
    """
    df = pd.read_csv(input_file, encoding="ISO-8859-1")

    df[["instruction", "input", "output", "text"]] = df.apply(
        lambda row: alpaca_columns(*info_from_csv(row, row.name + 1, cleanup)),
        axis=1,
        result_type="expand",
    )

    df = df[["instruction", "input", "output", "text"]]

    if textfile:
        save_first_instruction_to_file(df, textfile)

    if save:
        save_to_csv(df, output_file)
        
    print(f"Sample generated text (row {row_number}):")
    print(df.loc[row_number - 1, "text"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV and generate instructions.")
    parser.add_argument("--input", default="OnlyComments.csv", help="Input CSV file")
    parser.add_argument("--output", default="output.csv", help="Output CSV file")
    parser.add_argument("--textfile", default=None, help="Save first text col. row to file")
    parser.add_argument("--save", action="store_true", help="Save the DataFrame to a CSV file")
    parser.add_argument("--row", type=int, default=16, help="Row number to print (default: 3)")
    parser.add_argument("--cleanup", action="store_true", default=True, help="Remove multiple #")
    args = parser.parse_args()

    main(args.input, args.output, args.textfile, args.save, args.row, args.cleanup)