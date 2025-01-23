import requests
from django.conf import settings

def get_ollama_response(prompt):
    """
    Send a prompt to Ollama and return the response.
    """
    api_url = settings.OLLAMA_API_URL
    payload = {
        "model": "llama2",  # Replace with the model you pulled via Ollama
        "prompt": prompt,
        "stream": False  # Set to True if you want streaming responses
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from model")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama: {e}"
