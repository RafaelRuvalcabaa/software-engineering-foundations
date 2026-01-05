#Ejemplo diccionario 

persona = {
    "nombre": "Rafa",
    "edad": 23,
    "es_estudiante": False, 
    "calificaciones": [9,10,10],
    "socials":{
        "twitter": "@rafa",
        "facebook": "@rafa",
        "instagram": "@rafa"
    }
}

print(persona)

#Para acceder a los valores

print(persona["nombre"])
print(persona["calificaciones"][2])

#Cambiar valores al acceder 

persona["socials"]["facebook"] = "@rafita "

print(persona["socials"])

persona["nombre"] = "jose"
persona["calificaciones"][2] = 10

print(persona["nombre"])
print(persona["calificaciones"][2])

#Eliminar completamente una propiedad
del persona ["edad"]
print(persona)

es_estudiante = persona.pop("calificaciones")
print(f"es_estudiante: {es_estudiante}")
print(persona) 



#Sobreescribir un diccionario con otro diccionario...


a = {"name": "midu","age" :25 }
b = {"name": "rafa", "es_estudiante": True}

a.update(b)
print(a)


#Comprobar si existe una propiedad 
print("nombre" in persona)


#Obtener todos los valores
print("\nValores:")
print(persona.values())


#Obtener todas las claves 
print("\nKeys:")
print(persona.keys())


#Obtener tanto clave como valor 
print("\nItems :")
print(persona.items())
print("\n\n\n\n\n\n")

for key, value in persona.items():
    print(f"{key}: {value}")