# Expresiones regulares 

"""Las expresiones regulares son una secuencia de caracteres que forman un patron de busqueda. Se utilizan para la busqueda de cadena de texto, validacion de datos, etc...."""

"""¿Por que aprender las RegEx?

    -   Busqueda avanzada: Encontrar patrones especificos grandes y de forma rapida y precisa. (Editor de Markdown sólo usando RegEx)

    -   Validacion de datos: Asegurate que los datos que ingresa un usuario como el email, telefono, etc. sean correctos.

    -   Manipulacion del texto: Extraer, reemplazar y modificar partes de la cadena de texto facilmente.

"""

#1.- Importar el modulo de expresiones regualares. 
import re 

#2.- Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar 
pattern = "Hola"

#3.- El texto donde queremos buscar
text = "Hola mundo"

#4.- Usar la funcion de busqueda de "re"
resultado = re.search(pattern, text)

if resultado: 
    print("He encontrado el patron en el texto ", resultado.group())
else:
    print("No he encontrado el patrón en el texto")
    
#Devuelve la cadena que coincide con el patron 
print(resultado.group())


#.start() Devuelve la posicion inicial de la coincidencia 
print(resultado.start())


#.end() devolver la posicion final de la coincidencia 

print(resultado.end())