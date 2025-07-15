import os
import subprocess
import csv
# import unittest
# from dotenv import load_dotenv
# from hugchat import hugchat
# from hugchat.login import Login
import signal
import re

base_path = "submissionsPythonProjectsV3"
# user_input = "11111_234123.py"
env_name = "test"
csv_filename = "goodInputs.csv"  #  CSV filename you want to use
results_csv_filename = "ME21_Results2.csv"  # CSV file name output


def get_python_files_from_csv(csv_filepath):
    python_files = []
    with open(csv_filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            python_files.append((row["main_python_file_name"], row["FolderName"]))
    return python_files


# Old version that parses based on main.py file number
# def navigate_to_folder(base_path, user_input):
#     folder_name = user_input.split("_")[0]
#     folder_path = os.path.join(base_path, folder_name)

#     if os.path.exists(folder_path):
#         print(f"going to: {folder_path}")
#         os.chdir(folder_path)
#         print(f"current directory: {os.getcwd()}")
#     else:
#         print(f"Folder {folder_name} is not in {base_path}")
#         return None

#     return folder_path


def navigate_to_folder(base_path, folder_name):
    folder_path = os.path.join(base_path, folder_name)

    if os.path.exists(folder_path):
        print(f"going to: {folder_path}")
        os.chdir(folder_path)
        print(f"current directory: {os.getcwd()}")
    else:
        print(f"Folder {folder_name} is not in {base_path}")
        return None

    return folder_path


def concatenate_py_files(folder_path):
    concatenated_content = ""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".py"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                concatenated_content += file.read() + "\n"
    return concatenated_content


def find_import_lines(concatenated_content):
    import_lines = []
    lines = concatenated_content.splitlines()
    for line in lines:
        if "import" in line:
            import_lines.append(line.strip())
    return import_lines


def extract_install_packages(response):
    response_str = str(response)
    start_tag = "<install>"
    end_tag = "</install>"

    start_idx = response_str.find(start_tag)
    end_idx = response_str.find(end_tag)

    if (start_idx != -1) and (end_idx != -1):
        install_content = response_str[start_idx + len(start_tag) : end_idx].strip()
        packages = install_content.split()
        return packages
    return []


def write_requirements_txt(packages, file_path="requirements.txt"):
    with open(file_path, "w") as file:
        for package in packages:
            file.write(package + "\n")


def create_conda_environment(env_name):
    result = subprocess.run(["conda", "create", "-y", "-n", env_name, "python"], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"'{env_name}' created successfully.")
    else:
        print(f"Failed to create conda environment '{env_name}':")
        print(result.stderr)



def install_requirements(env_name, requirements_file="requirements.txt"):

    env_check = subprocess.run(["conda", "env", "list"], capture_output=True, text=True)
    env_list = env_check.stdout.strip().split("\n")
    env_exists = any(env_name in line and os.path.isdir(line.split()[-1]) for line in env_list if line and not line.startswith("#"))

    if not env_exists:
        print(f"Environment '{env_name}' does not exist. Skipping package installation.")
        print("Available environments:\n", env_check.stdout)
        return

    with open(requirements_file, "r") as file:
        packages = [line.strip() for line in file if line.strip()]

    print(f"Installing packages into conda environment '{env_name}': {packages}")

    for package in packages:
        result = subprocess.run(
            ["conda", "run", "-n", env_name, "pip", "install", package],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"Failed to install package: {package}")
            print("stderr:\n", result.stderr)
        else:
            print(f"Successfully installed package: {package}")


def check_conda_environment(env_name):
    result = subprocess.run(["conda", "env", "list"], capture_output=True, text=True)
    envs = result.stdout.strip().split("\n")

    for line in envs:
        if line.startswith("#") or not line.strip():
            continue

        parts = line.strip().split()
        if len(parts) >= 2:
            env_name_col, env_path = parts[0], parts[-1]
            if env_name_col == env_name or os.path.basename(env_path) == env_name:
                return True

    return False


def list_installed_packages(env_name):
    result = subprocess.run(["conda", "list", "-n", env_name], capture_output=True, text=True)
    print(f"Installed packages in conda '{env_name}':\n{result.stdout}")


def delete_conda_environment(env_name):
    subprocess.run(["conda", "remove", "-y", "--name", env_name, "--all"])
    print(f"'{env_name}' deleted")


def create_bash_script(env_name, script_path, formatted_inputs=None):
    if formatted_inputs:
        bash_script_content = f"""
        #!/bin/bash
        source $(conda info --base)/etc/profile.d/conda.sh
        conda activate {env_name}
        echo -e "{formatted_inputs}" | python {script_path}
        if [ $? -ne 0 ]; then
            echo "Python script failed"
            exit 1
        fi
        conda deactivate
        """
    else:
        bash_script_content = f"""
        #!/bin/bash
        source $(conda info --base)/etc/profile.d/conda.sh
        conda activate {env_name}
        python {script_path}
        if [ $? -ne 0 ]; then
            echo "Python script failed"
            exit 1
        fi
        conda deactivate
        """

    script_file = "run_script.sh"
    with open(script_file, "w") as file:
        file.write(bash_script_content)
    os.chmod(script_file, 0o755)
    return script_file


def run_python_script_interactive(script_file, timeout=20, interactive=False):
    def handler(signum, frame):
        raise TimeoutError("Script timed out")

    if interactive:
        result = subprocess.Popen(["bash", script_file])
        result.communicate()
    else:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        try:
            result = subprocess.run(["bash", script_file], capture_output=True, text=True)
            signal.alarm(0)
            if result.returncode == 0:
                print("Script ran successfully.")
                result_msg = "Script ran successfully"
            else:
                if "EOFError: EOF when reading a line" in result.stderr:
                    result_msg = "Did not run test to check if code crashes."
                    print(result_msg)
                else:
                    print(f"Script crashed with error code {result.returncode}")
                    error_lines = result.stderr.strip().split("\n")
                    error_lines = error_lines[2:]
                    filtered_error = "\n".join(error_lines)
                    print("Error:\n", filtered_error)
                    result_msg = f"Script crashed\nError: {filtered_error}"
        except TimeoutError:
            result_msg = "Did not run test to check if code crashes."
            print(result_msg)

    return result_msg


def get_packages(chatbot, student_submission):
    queries = f"write a requirements.txt of the package names to install the 3rd party packages for the code below. Dont explain. Write them between only one pair of <install> </install> tags:\n\n<code>\n{student_submission}\n</code>"
    print(queries)

    try:
        query_result = chatbot.query(queries)
        print(query_result)
        packages = extract_install_packages(query_result)
        return packages
    except Exception as e:
        print(f"error connecting: {e}")
        print("continuing on")
        return []


def get_inputs_for_main_file(csv_filepath, main_python_file_name):
    inputs = []
    with open(csv_filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["main_python_file_name"] == main_python_file_name:
                for key in row:
                    if key.startswith("input_"):
                        value = row[key].strip()
                        if value:  
                            inputs.append(value)
                        else:  
                            break
                break
    formatted_inputs = "\n".join(inputs)
    print(f"Inputs for {main_python_file_name}: {formatted_inputs}")  
    return formatted_inputs


def get_imports_for_main_file(csv_filepath, main_python_file_name):
    with open(csv_filepath, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["main_python_file_name"] == main_python_file_name:
                imports_field = row.get("imports", "").strip()
                if imports_field:
                    packages = [pkg.strip() for pkg in imports_field.split(",") if pkg.strip()]
                    print(f"Imports for {main_python_file_name}: {packages}")
                    return packages
                break
    return []


def log_result_to_csv(csv_filename, main_python_file_name, result_code, current_dir):
    sanitized_result_code = (
        result_code.replace("\n", "\\n")
        .replace("\r", "\\r")
        .replace(",", "\\,")
        .replace('"', '""')
    )

    csv_filepath = os.path.join(current_dir, csv_filename)
    file_exists = os.path.isfile(csv_filepath)

    with open(csv_filepath, mode="a", newline="") as csvfile:
        fieldnames = ["main_python_file_name", "result"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(
            {"main_python_file_name": main_python_file_name, "result": sanitized_result_code}
        )


def main():
    current_dir = os.getcwd()
    csv_filepath = os.path.join(current_dir, csv_filename)

    # the list of tuples (main_python_file_name, FolderName) from the CSV
    x = get_python_files_from_csv(csv_filepath)
    print(x)
    for main_python_file_name, folder_name in x:

        # folder_name directly for navigating
        folder_path = navigate_to_folder(os.path.join(current_dir, base_path), folder_name)
        print(f"folder {folder_path}")
        
        if folder_path:
            concatenated_content = concatenate_py_files(folder_path)
            import_lines = find_import_lines(concatenated_content)

            if not check_conda_environment(env_name):
                create_conda_environment(env_name)

            requirements_file_path = os.path.join(folder_path, "requirements.txt")
            if os.path.exists(requirements_file_path):
                print(f"'requirements.txt' already found in {folder_path}, skipping query")
                install_requirements(env_name, requirements_file_path)
            else:
                print(f"No requirements.txt found in {folder_path}. Attempting to build it from CSV imports column...")
                packages = get_imports_for_main_file(csv_filepath, main_python_file_name)
                if packages:
                    write_requirements_txt(packages, requirements_file_path)
                    install_requirements(env_name, requirements_file_path)
                else:
                    print(f"No import packages found in CSV for {main_python_file_name}. Skipping installation.")


            # else:
            #     '''This part is for hugchat but don't need since all files should have requirements now or no import lines found'''

                # if import_lines:
                #     import_lines_str = "\n".join(import_lines)
                #     print(import_lines_str)
                #     student_submission = import_lines_str

                #     load_dotenv()
                #     email = os.getenv("EMAIL")
                #     passwd = os.getenv("PASSWORD")

                #     sign = Login(email, passwd)
                #     cookie_path_dir = "./cookies_snapshot"
                #     sign.saveCookiesToDir(cookie_path_dir)
                #     cookies = sign.loadCookiesFromDir(cookie_path_dir)

                #     chatbot = hugchat.ChatBot(cookies=cookies.get_dict(), default_llm=1)

                #     max_packages = []
                #     for _ in range(3):
                #         packages = get_packages(chatbot, student_submission)
                #         if len(packages) > len(max_packages):
                #             max_packages = packages

                #     write_requirements_txt(max_packages)
                #     install_requirements(env_name, requirements_file_path)
                # else:
                # print("no import statements found in the files")   #if uncommenting top then indent this line

            list_installed_packages(env_name)

            script_path = os.path.join(folder_path, main_python_file_name)
            print(f"running '{script_path}' in conda '{env_name}'...")

            # use_csv = input("Do you want to use CSV file for inputs? (yes/no): ").strip().lower()
            use_csv = "yes"
            if use_csv == "yes":
                formatted_inputs = get_inputs_for_main_file(csv_filepath, main_python_file_name)
                bash_script = create_bash_script(env_name, script_path, formatted_inputs)
                result_msg = run_python_script_interactive(bash_script)
                log_result_to_csv(
                    results_csv_filename, main_python_file_name, result_msg, current_dir
                )
            else:
                try:
                    bash_script = create_bash_script(env_name, script_path)
                    result_msg = run_python_script_interactive(bash_script, interactive=True)
                except KeyboardInterrupt:
                    result_msg = "Script interrupted by user"
                    print(result_msg)
                log_result_to_csv(
                    results_csv_filename, main_python_file_name, result_msg, current_dir
                )

            # delete_env = (
            #     input(f"do you want to delete the conda environment '{env_name}'? (yes/no): ")
            #     .strip()
            #     .lower()
            # )
            delete_env = "yes"
            if delete_env == "yes":
                delete_conda_environment(env_name)
            else:
                print(f"you're keeping '{env_name}'.")


if __name__ == "__main__":
    main()
