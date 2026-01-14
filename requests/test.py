# Como hacer peticiones a APIs con python. Sin y con dependencias externas. 

# 1.- Sin dependencias. (Dificil y sin dependencias externas).

# Importar librerias necesarias.
import urllib.request
# Urllib para hacer peticiones HTTP.
import json 
# JSON para manejar datos en formato JSON.

# Guardar la URL de la API en una variable.
api_posts = "https://jsonplaceholder.typicode.com/posts"

# Lo mejor es usar try-except para manejar errores en las peticiones.
try: 
    # Hacer la peticion a la API.
    # Guaradar la respuesta en una variable. Con urlopen de urllib. 
    response = urllib.request.urlopen(api_posts)

    # Leer los datos de la respuesta
    data = response.read()
    # Convertir los datos de JSON a un diccionario de Python y decodearlos a UTF-8.
    json_data = json.loads(data.decode("utf-8"))

    print(json_data)

    # Cerrar la respuesta para liberar recursos.
    response.close() 
except urllib.error.URLError as e: 
    print(f"Error en la solicitud: {e.reason}")


#2.- Con dependencias externas. (Mas facil y recomendado).
import requests

# Usar un try except para manejar errores en las peticiones.
try: 
    print("\n\n\nGET:")
     # Hacer la peticion GET a la API y guardar la respuesta en una variable.
    response = requests.get(api_posts)
    # Imprimir el contenido de la respuesta en formato JSON.
    print(response.json())
    #Acceder a un recurso especifico, por ejemplo el post con id 1 que es la posicion 0 en la lista.
    print("\n\n\nGET post id 1:")
    json = response.json()
    print(json[0])

# Except para manejar errores en la peticion.
# requests.exceptions es una clase base para todas las excepciones de requests.
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

