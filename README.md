# **User Guide: Cloning and Running the LangChain Test Report Analyzer**

## **📌 Overview**

The **LangChain Test Report Analyzer** automates the process of analyzing software test reports. It:

- Generates a **JUnit test report** from automated tests.
- Parses the report to extract **failed test cases**.
- Uses **LangChain with Ollama** to analyze failures and provide **root cause insights**.
- Summarizes test results into a **human-readable report**.

This tool helps software testers quickly diagnose test failures and improve debugging efficiency.
This guide explains how to clone the LangChain Test Report Analyzer project onto your local machine, set up the environment, install dependencies, and run the analysis.

---
## **🔧 Pre-Requisites**
Before you begin, ensure you have the following installed on your machine:

- **Python 3.8+** (Check with `python --version` or `python3 --version`)
- **Git** (Required for cloning the repository)
- **Ollama with Llama 3 Model**
  - Install Ollama: [https://ollama.ai](https://ollama.ai)
  - Pull the required model:
    ```sh
    ollama pull llama3
    ```
  - Verify the model is available:
    ```sh
    ollama list
    ```

If `llama3` is not listed, restart Ollama and try pulling the model again.

## **🛠 Step 1: Clone the Project**

### **1.1 Clone the Repository**
1. Open **Visual Studio Code** (or your preferred terminal).
2. Run the following command to clone the project:
   ```sh
   git clone <your-repo-url> langchain_test_analyzer
   cd langchain_test_analyzer
   ```

---
## **🖥 Step 2: Set Up the Virtual Environment**
A virtual environment ensures that dependencies are isolated.

### **2.1 Create and Activate the Virtual Environment**

#### **For Windows (PowerShell or CMD)**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **For macOS/Linux (Terminal)**
```sh
python3 -m venv venv
source venv/bin/activate
```

✅ If successful, your terminal will now show `(venv)` at the beginning of the line.

---
## **📦 Step 3: Install Dependencies**

### **3.1 Install Required Libraries**
Once the virtual environment is activated, install the required dependencies using:
```sh
pip install -r requirements.txt
```

### **3.2 Verify Installation**
To confirm everything is installed correctly, run:
```sh
python -c "import langchain; print('LangChain Installed Successfully!')"
```
If no errors appear, the setup is complete.

---
## **📝 Step 4: Generate a Test Report**

JUnit reports are required for analysis. If you don't have a report, generate one using `pytest`.

### **4.1 Run Sample Tests to Create a Report**
1. Run the test suite to generate a test report:
   ```sh
   pytest --junitxml=test_report.xml
   ```
2. After running, `test_report.xml` should appear in your project folder.

---
## **📊 Step 5: Parse the Test Report**
Now, extract failed test cases from the report.

### **5.1 Run the Report Parsing Script**
1. Execute the parsing script to extract failure details:
   ```sh
   python parse_report.py
   ```
2. If successful, it will output a list of failed test cases and their error messages.

---
## **🤖 Step 6: Analyze the Failures**
Use LangChain and Ollama to analyze test failures and suggest potential root causes.

### **6.1 Ensure Ollama is Running**
If using Ollama, confirm the model is available:
```sh
ollama pull llama3
ollama list
```
If `llama3` is not listed, restart Ollama and pull the model again.

### **6.2 Run the Failure Analysis Script**
Run the analysis script to get insights into test failures:
```sh
python analyze_failures.py
```
✅ This will output AI-generated insights on possible failure causes.

---
## **📌 Step 7: Generate a Test Summary**
Summarize the overall results from the test analysis.

### **7.1 Run the Summary Function**
1. The failure analysis script also generates a summary. If needed, rerun it:
   ```sh
   python analyze_failures.py
   ```
2. The script will display:
   - **Root causes of failures**
   - **A summarized test report**

---
## **📈 Future Enhancements**
To improve and expand the functionality of the LangChain Test Report Analyzer, consider the following enhancements:

🔹 **Integration with JIRA or Bug Tracking Tools** – Automatically create JIRA tickets for failed test cases, linking them with analysis insights.

🔹 **Historical Analysis & Vector Search** – Store past test failures in a vector database and use similarity search to detect recurring issues.

🔹 **Web-Based Dashboard** – Develop a simple front-end to visualize test results, failure insights, and trends over time.

🔹 **Multi-Model Support** – Experiment with different LLMs (e.g., GPT-4, Mistral) to compare analysis accuracy and insights.

🔹 **Automated Reporting** – Generate HTML/PDF reports summarizing failures and suggestions for easy sharing.

---
## **🚀 Final Notes**

✅ **Congratulations!** You have successfully set up and run the LangChain Test Report Analyzer.

### **Troubleshooting**
- If `pytest` fails, ensure dependencies are installed: `pip install -r requirements.txt`
- If `OllamaEndpointNotFoundError` occurs, ensure the model is available by running:
  ```sh
  ollama pull llama3
  ollama list
  ```
- If the `parse_report.py` script does not return failures, check if `test_report.xml` was created properly.

For improvements, consider:
🔹 **Integrating with JIRA** – Automatically log failures.  
🔹 **Using Vector Search** – Store past failures for pattern analysis.  
🔹 **Adding a Web UI** – Display results in a dashboard.

**Now you’re ready to analyze test results efficiently! 🚀**

