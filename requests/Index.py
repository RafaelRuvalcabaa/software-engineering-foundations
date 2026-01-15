# Usar la API de GPT-4o de OpenAI  

# ref making requests to OpenAI's GPT-4o API: https://platform.openai.com/docs/guides/gpt/gpt-4o

import requests

OPENAI_API_KEY = "API_KEY, genera una aqui: https://platform.openai.com/account/api-keys"


def call_openai_gpt( prompt):
    url = "https://api.openai.com/v1/responses/resp_123"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }       

    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=data)
    print(response.json())

call_openai_gpt(OPENAI_API_KEY, "Hola, ¿Como ves mi codigo?")