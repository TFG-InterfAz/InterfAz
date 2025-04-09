from openai import OpenAI
from dotenv import load_dotenv
from textwrap import dedent

load_dotenv()
client = OpenAI(api_key="sk-a7573b42a5c449aaab06693c80930861", base_url="https://api.deepseek.com")

def get_form_response(prompt):
    system_prompt = """
        You are an AI that generates HTML forms based on user prompts.
        Your task is to take a description of a form and output the corresponding form fields and structure.
    """
    completion = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": dedent(system_prompt)},
            {"role": "user", "content": prompt},
        ],
        stream=False

    )
    return completion.choices[0].message.content

