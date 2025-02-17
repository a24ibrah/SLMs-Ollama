Small LLMs & Ollama: Automating AI on Local Machines

📖 Overview

This project provides an automated pipeline for downloading, fine-tuning, and deploying small language models (LLMs) using Ollama. Additionally, it includes a synthetic dataset generator that creates meaningful text classification data for training AI models.

By following this guide, you'll be able to:

Generate synthetic training data for LLM fine-tuning.

Automate the process of fine-tuning a small LLM.

Deploy and run an optimized model on your local machine using Ollama.

Run a report script to evaluate the performance of the fine-tuned model.

📁 Project Structure

/your_project/
│── automate_llm.py            # The automation script for small LLMs
│── generate_synthetic_data.py # Script to generate synthetic dataset
│── requirements.txt           # Dependencies for the project
│── synthetic_data.csv         # The generated dataset
│── report.py                  # Script to generate a performance report

🛠️ Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/your-repo/ollama-llm-automation.git
cd ollama-llm-automation

2️⃣ Install Dependencies

Ensure you have Python 3.8+ installed, then install the required dependencies:

pip install -r requirements.txt

3️⃣ Install Ollama

Ollama is required to fine-tune and run the AI model locally. Download and install it from:
🔗 Ollama Official Website

Verify installation:

ollama --version

📊 Generating Synthetic Data

This project includes a synthetic data generator that creates realistic text classification data (e.g., customer support queries).

Generate the Dataset

python generate_synthetic_data.py

This will create synthetic_data.csv, a dataset containing text samples and their respective labels.

📌 Example (CSV Format):

customer_query

category

My bill amount is incorrect. Can you check my latest invoice?

Billing Issue

I am unable to log into my account. It keeps showing an error.

Technical Support

How do I update my email and password for my account?

Account Management

⚙️ Automating the Fine-Tuning and Deployment

The script automate_llm.py streamlines the entire LLM fine-tuning and deployment process.

Run the Full Automation Pipeline

python automate_llm.py

This script will:

Download a small LLM (DistilBERT by default).

Fine-tune the model using the synthetic dataset.

Export the fine-tuned model for deployment.

Run the trained model to generate predictions.

📊 Running the Report Script

The report.py script evaluates the performance of the fine-tuned model. It can measure accuracy, precision, recall, and other key metrics.

Generate a Model Performance Report

python report.py

📌 Metrics Included in the Report:

Model Accuracy

Precision & Recall

Sample Predictions & Errors

🚀 Next Steps

🔹 Customize the dataset: Modify generate_synthetic_data.py to add more categories.🔹 Experiment with different LLMs: Change the model_name in automate_llm.py.🔹 Deploy AI in production: Integrate with a chatbot or a business workflow.

💡 Questions or Contributions? Open an issue or submit a pull request!

📌 License

MIT License - Feel free to modify and use this project!

Enjoy building AI-powered solutions with SLMs & Ollama! 