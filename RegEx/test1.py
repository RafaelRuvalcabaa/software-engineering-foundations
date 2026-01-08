import re

target = "IA"

text = "La inteligencia artificial avanza rápidamente y se integra en múltiples áreas de la vida diaria, desde la automatización hasta el análisis de datos complejos. En medio de este desarrollo, IA aparece como un concepto clave que redefine la forma en que interactuamos con la tecnología."


found_AI = re.search(target, text)

if found_AI: 
    print(f"He encontrado el patrón en la posicion {found_AI.start()} y termina en la posicion {found_AI.end()}")
else: 
    print("No lo he encontrado")

#---------------------

### Encontrar todas la coincidencias en un patrón 

# .findall() devuelve una lista con todas las coincidencias. 


texto = "Python avanza rápidamente y Python se integra en múltiples áreas del desarrollo tecnológico. Gracias a Python, la automatización y el análisis de datos son más accesibles. En este contexto, Python se posiciona como una herramienta clave que redefine la forma en que interactuamos con la tecnología mediante soluciones creadas con Python."

pattern = "P.thon"

matches = re.findall(pattern, texto)

print(len(matches))



#------------------------------- 
# Iter()
# Devuelve un iterador que contiene todos los resultados de la búsqueda  


texto = "Python avanza rápidamente y Python se integra en múltiples áreas del desarrollo tecnológico. Gracias a Python, la automatización y el análisis de datos son más accesibles. En este contexto, Python se posiciona como una herramienta clave que redefine la forma en que interactuamos con la tecnología mediante soluciones creadas con Python."

pattern = "Python"

matches = re.finditer(pattern, texto)

for match in matches: 
    print(match.group(), match.start(), match.end())



#-------------------------------### Modificaciones 

# Los modificacadores son opciones que se pueden agregar a un patron para camianr su comportamiento. 

# re.IGNORECASE: Ignora las mayúsculas y minusculas 

look_for = "carro"

where_i_can_find = "El carro forma parte de la vida diaria y el Carro es un medio esencial de transporte. Con el CARRO se facilita la movilidad y el uso del carro permite desplazamientos más rápidos. En este contexto, el Carro se mantiene como un elemento clave en la rutina cotidiana. cArRo"



mattches = re.findall(look_for, where_i_can_find, re.IGNORECASE)

if mattches: 
    print(f"Se encontró {len(mattches)} veces")
    print(f"Se encontró de las siguientes maneras: {mattches}")


#------------------------

### Remplazar el texto 

text = "Hola, mundo! Hola de nuevo...."

pattern = "Hola"

replacement = "Bienvenido"

# Count es para decirle las veces que quiere remplazar esa palabra del texto, por ejemplo, habia dos veces "Hola" y solo cambio la primera... 


newText = re.sub(pattern, replacement,text, count = 1)

print(newText)