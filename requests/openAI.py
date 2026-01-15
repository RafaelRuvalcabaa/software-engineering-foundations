import os
import requests

# Ref para crear o modificar mi clave API de OpenAI: https://platform.openai.com/account/api-keys
# Asegúrate de tener la variable de entorno:
# export OPENAI_API_KEY="tu_api_key"

OPENAI_API_KEY = "tu_api_key_aqui"

def call_openai_gpt(prompt):
    url = "https://api.openai.com/v1/responses"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    data = {
        "model": "gpt-4.1-mini",
        "input": prompt
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["output"][0]["content"][0]["text"]

print(call_openai_gpt("Hola, ¿cómo ves mi código?"))
