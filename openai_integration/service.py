import openai
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()
client = openai.OpenAI(api_key="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")

def get_form_response(prompt):
    system_prompt = """
        You are an AI that generates HTML forms based on user prompts.
        Your task is to take a description of a form and output the corresponding form fields and structure.
    """
    completion = client.beta.chat.completions.parse(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": dedent(system_prompt)},
            {"role": "user", "content": prompt},
        ],
        #response_format=DynamicForm,
    )
    return completion.choices[0].message

