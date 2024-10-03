from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_startup_name_and_items(domain):
    # Chain 1: Startup_name
    prompt_template_name = PromptTemplate(
        input_variables=['domain'],
        template="I want to establish a startup in the {domain}. Please suggest only one fancy name"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="startup_name")

    # Chain 2: startup Items
    prompt_template_items = PromptTemplate(
        input_variables=['startup_name'],
        template="""Please provide description for {startup_name} idea """
    )

    startup_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="startup_items")

    chain = SequentialChain(
        chains=[name_chain, startup_items_chain],
        input_variables=['domain'],
        output_variables=['startup_name', "startup_items"]
    )

    response = chain({'domain': domain})

    return response

if __name__ == "__main__":
    print(generate_startup_name_and_items("Health"))
