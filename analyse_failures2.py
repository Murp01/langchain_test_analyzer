from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import parse_report

# Load the LLM
llm = Ollama(model="llama3")

summary_prompt = PromptTemplate(
    input_variables=["analysis"],
    template="Summarize the test report: \n\n{analysis}"
)

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

def summarize_results(analysis):
    chain = LLMChain(llm=llm, prompt=summary_prompt)
    return chain.run(analysis)

# Run Analysis
failures = parse_report.parse_junit_report("test_report.xml")
failure_messages = "\n".join([f"{f['test']}: {f['message']}" for f in failures])

analysis = analyze_failures(failure_messages)
#thiprint("\n💡 Analysis:\n", analysis)

summary = summarize_results(analysis)
print("\n📌 Test Summary:\n", summary)