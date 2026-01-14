# Como hacer peticiones a APIs con python. Sin y con dependencias externas. 

# 1.- Sin dependencias. (Dificil y sin dependencias externas).

# Importar librerias necesarias.
import urllib.request
# Urllib para hacer peticiones HTTP.
import json 
# JSON para manejar datos en formato JSON.

# Guardar la URL de la API en una variable.
api_posts = "https://jslaceholder.typicode.com/posts"

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