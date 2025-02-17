import os
import subprocess
from transformers import AutoModelForCausalLM, AutoTokenizer

# Step 1: Install Ollama (Assumes Ollama is installed manually)
def check_ollama_installation():
    try:
        version = subprocess.check_output(["ollama", "--version"]).decode("utf-8").strip()
        print(f"Ollama is installed. Version: {version}")
    except FileNotFoundError:
        print("Ollama is not installed. Please install it from https://ollama.ai before running this script.")
        exit()

# Step 2: Download a Small LLM
def download_model(model_name="distilbert-base-uncased"):
    print(f"Downloading model: {model_name}...")
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    print(f"Model {model_name} downloaded successfully.")
    return model, tokenizer

# Step 3: Fine-tune the Model
def fine_tune_model(model_name="distilbert-base-uncased", dataset_path="my_data.csv"):
    print(f"Fine-tuning {model_name} with dataset: {dataset_path}...")
    cmd = [
        "ollama", "fine-tune",
        "--model", model_name,
        "--dataset", dataset_path,
        "--task", "text-classification"
    ]
    subprocess.run(cmd)
    print("Fine-tuning complete.")

# Step 4: Export the Fine-Tuned Model
def export_model(model_name="fine-tuned-distilbert", output_path="my_fine_tuned_model"):
    print(f"Exporting fine-tuned model to {output_path}...")
    cmd = ["ollama", "export", "--model", model_name, "--output", output_path]
    subprocess.run(cmd)
    print("Model export complete.")

# Step 5: Deploy and Run the Model
def run_model(model_name="my_fine_tuned_model", input_text="Hello, how can AI help?"):
    print(f"Running model: {model_name} with input: {input_text}")
    cmd = ["ollama", "run", "--model", model_name, "--input", input_text]
    result = subprocess.check_output(cmd).decode("utf-8").strip()
    print(f"Model Output:\n{result}")

# Run the automation pipeline
if __name__ == "__main__":
    check_ollama_installation()  # Step 1
    download_model()  # Step 2
    fine_tune_model()  # Step 3
    export_model()  # Step 4
    run_model()  # Step 5
