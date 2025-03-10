# **LangChain Test Report Analyzer - Step-by-Step Guide**

## **📌 Overview**
This guide will help you set up and use LangChain to analyze test reports using **Ollama** with **Llama 3.1**. We'll start from scratch, ensuring every step is covered for beginners. The guide assumes you're using **Visual Studio Code**.

---
## **🛠 Step 1: Setting Up the Project**

### **1.1 Clone the Repository and Create a Project Folder**
1. Open **Visual Studio Code**.
2. Clone the repository if you're setting up an existing project:
   ```sh
   git clone <your-repo-url> langchain_test_analyzer
   cd langchain_test_analyzer
   ```
3. If you're starting fresh, create a new folder for your project:
   ```sh
   mkdir langchain_test_analyzer
   cd langchain_test_analyzer
   ```

### **1.2 Set Up a Virtual Environment**
A virtual environment helps isolate dependencies and avoids conflicts with system-installed packages.

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
## **📦 Step 2: Install Dependencies**

All required dependencies are listed in `requirements.txt`. First, ensure the file exists by creating it in the **project root** (`langchain_test_analyzer` folder):

### **2.1 Create `requirements.txt`**
1. In the **project root**, create a new file named `requirements.txt`.
2. Add the following dependencies:

```txt
langchain
ollama
pandas
xmltodict
beautifulsoup4
tiktoken
pytest
pytest-xml
data_to_xml
```

### **2.2 Install Dependencies**
Run the following command to install all dependencies from `requirements.txt`:
```sh
pip install -r requirements.txt
```

🔍 **Verify Installation:**
Run the following to check if `langchain` is installed:
```sh
python -c "import langchain; print('LangChain Installed Successfully!')"
```
If no errors appear, you're good to go.

---
## **📝 Step 3: Generate a Sample JUnit Test Report**

JUnit reports are typically XML files. We'll generate one using a Python testing framework.

### **3.1 Create a Sample Test File**
1. Inside your project folder, create a new folder called `tests`.
2. Inside `tests`, create a file called `test_example.py`.
3. Add the following code:

```python
import pytest

def test_success():
    assert 1 + 1 == 2

def test_failure():
    assert 1 + 1 == 3

def test_api():
    response_status = 500  # Simulating API failure
    assert response_status == 200
```

### **3.2 Run Tests and Generate a Report**
Run the tests and generate a JUnit report:
```sh
pytest --junitxml=test_report.xml
```

After running, you should see `test_report.xml` in your project folder.

---
## **📊 Step 4: Load & Parse the JUnit Test Report**

Now, let's use Python to read and extract failed test cases.

### **4.1 Create a Python Script**
1. Create a new file called `parse_report.py` in the **project root** (`langchain_test_analyzer` folder).
2. Add the following code:

```python
import xml.etree.ElementTree as ET

def parse_junit_report(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    failures = []

    for testcase in root.findall(".//testcase"):
        failure = testcase.find("failure")
        if failure is not None:
            failures.append({
                "test": testcase.attrib["name"],
                "message": failure.attrib["message"]
            })
    
    return failures

# Test parsing
failures = parse_junit_report("test_report.xml")
print(failures)
```

Run it:
```sh
python parse_report.py
```
If successful, it should print the failed tests.

---
## **🤖 Step 5: Use LangChain to Analyze Failures**

### **5.1 Create a New Script: `analyze_failures.py` in the project root (`langchain_test_analyzer` folder).**
```python
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import parse_report

# Load the LLM
llm = Ollama(model="llama3")

# Define Prompt
prompt = PromptTemplate(
    input_variables=["failures"],
    template="""
Analyze these test failures and suggest possible root causes:
{failures}
"""
)

# Create LangChain Chain
def analyze_failures(failures):
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(failures)

# Run Analysis
failures = parse_report.parse_junit_report("test_report.xml")
failure_messages = "\n".join([f"{f['test']}: {f['message']}" for f in failures])

analysis = analyze_failures(failure_messages)
print("\n💡 Analysis:\n", analysis)
```

Run it:
```sh
python analyze_failures.py
```
✅ This will analyze failures and suggest possible root causes.

---
## **📝 Step 6: Generate a Test Summary**

Add a summary function to `analyze_failures.py`:

```python
summary_prompt = PromptTemplate(
    input_variables=["analysis"],
    template="Summarize the test report:\n{analysis}"
)

def summarize_results(analysis):
    chain = LLMChain(llm=llm, prompt=summary_prompt)
    return chain.run(analysis)

summary = summarize_results(analysis)
print("\n📌 Test Summary:\n", summary)
```

Run it again to see the summary:
```sh
python analyze_failures.py
```

---
## **🚀 Next Steps**

🔹 **Improve error handling** – Handle missing reports or empty test cases.  
🔹 **Use vector search** – Store past failures and retrieve similar issues.  
🔹 **Integrate with JIRA** – Automatically log issues based on analysis.  
🔹 **Create a Web UI** – Display results in a dashboard.

🎯 **Congratulations! You've built an AI-powered Test Report Analyzer!** 🚀

