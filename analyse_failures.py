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