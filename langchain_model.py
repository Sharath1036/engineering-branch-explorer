from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('GROQ_API_KEY')
# print(api_key)

llm = ChatGroq(temperature=0, model_name="llama-3.1-70b-versatile")

def branch_overview(branch):

    # Chain 1: Salary
    branch_name = PromptTemplate(
    input_variables = ['branch'],
    template = "What is the entry-level salary for {branch} engineering stream in India?"
)
    
    # Chain 2: Syllabus
    syllabus_prompt = PromptTemplate(
    input_variables = ['stream'],
    template = "What is the syllabus for B.Tech in {stream} for all the eight semesters in India?"
)
    
    branch_chain = LLMChain(llm=llm, prompt=branch_name, output_key='stream')
    syllabus_chain = LLMChain(llm=llm, prompt=syllabus_prompt, output_key='syllabus')

    # Sequential Chain
    chain = SequentialChain(
    chains = [branch_chain, syllabus_chain],
    input_variables = ['branch'],
    output_variables = ['stream', 'syllabus']
)
    
    result = chain({"branch": branch})

    return result

if __name__ == "__main__":
    print(branch_overview("Data Science"))