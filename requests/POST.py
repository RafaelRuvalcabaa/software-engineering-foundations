
# 3.- Hacer un POST a la API de jsonplaceholder con requests.


# Importamos requests para poder hacer la peticion POST.
import requests 


print("\n\n\nPOST:")

# Guardar la URL de la API en una variable.
api_posts = "https://jsonplaceholder.typicode.com/posts"

# Hacer la peticion POST a la API, usando reques.ts.post y pasando un diccionario con los datos a enviar en formato JSON.
try: 
    response = requests.post(api_posts, json={
        "title": "my new post",
        "body": "lorem ipsum dolor sit amet",
        "userId": 1
    }) 
    # Imprimir la respuesta en formato JSON.
    print(response.json())
    print(f"Status code: {response.status_code}")

except requests.exceptions.RequestException as event: 
    print("Error en la solicitud POST:", event)