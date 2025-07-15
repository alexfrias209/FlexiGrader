# **FlexiGrader**

An LLM-based personalized autograder for student code submissions.  
It uses a fine-tuned model and an execution environment to evaluate code quality, logic, and structure on diverse projects — enabling scalable, consistent, and customizable grading.

---

## 📁 Folder Structure

The project expects student submissions to be structured like this:

<pre>
MainFolderContainingAllStudents/
├── StudentIDFolder1/
│   ├── StudentCodePythonScripts1.py
│   ├── ...
│   └── StudentCodePythonScriptsN.py
├── StudentIDFolder2/
│   ├── StudentCodePythonScripts1.py
│   ├── ...
│   └── StudentCodePythonScriptsN.py
├── ...
└── StudentIDFolderN/
    ├── StudentCodePythonScripts1.py
    ├── ...
    └── StudentCodePythonScriptsN.py
</pre>

---

## 🚀 Setup & Run Everything

To set up the environment and test out the autograder and model inference, follow these steps:

```bash
# Step 1: Create and activate the Conda environment
conda create -n flexigrader python=3.10.15 -y
conda activate flexigrader
pip install -r requirements.txt

# Step 2: Test to run the execution
cd components
python execution.py

# Step 3: Test to run the model (Need A100 80GB GPU)
# Download the test dataset first and then run:
python getTestInfereceData.py
python model_inference.py
```

---

## 🔗 Model Checkpoint

This project uses a fine-tuned version of Code LLaMA 34B, available here:

👉 **[Hugging Face – afrias5/codellama34b_finetuned](https://huggingface.co/afrias5/codellama34b_finetuned)**

---

## 🧩 Third-Party Components

This project includes code from:

- **[Axolotl](https://github.com/axolotl-ai-cloud/axolotl)** – Apache 2.0 license

---

## 📄 License

- **FlexiGrader**: [Apache License 2.0 License](./LICENSE) 
- **Axolotl code in `axolotl/`**: Apache 2.0 (see `axolotl/LICENSE`)
