###
# ------------ Meta caracteres 
# Los metacaracteres son simbolos especiales con significados especificos en las expresiones reguales. 
### 

import re 

#1.- El punto (.)
# Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H#la otra vez"

pattern = "H.la"
 

found = re.findall(pattern, text)

if(found):
    print(found)
else: 
    print("No se encontro ninguna coincidencia...")


text = "casa caasa cosa cisa cessa cesa causa"


pattern = "c.sa"

found = re.findall(pattern, text)

if(found):
    print(found)
    print(f"Se encotró {len((found))} veces")
else: 
    print("No se encontraron coincidencias....")


#---------------------
text = "casa caasa cosa cisa cessa cesa causa"
# Con la R estamos indicando que es una expresion regular 
pattern = r"c.sa"

found = re.findall(pattern, text)

if(found):
    print(found)
    print(f"Se encotró {len((found))} veces")
else: 
    print("No se encontraron coincidencias....")


#-------------------------------
### Con el punto busca cada carater y por lo mismo imprime cada valor separado 

text = "Mi casda es blanca y mi coche negro."

pattern = "."

matches = re.findall(pattern, text)

print(matches)

#-------------------------------
### Ahora si con esta expresión buscas los puntos. 
### Esto se hace con diagonal invertida antes del punto.

text = "Mi. cas.da es. blanca y mi coche negro."

pattern = r"\."

matches = re.findall(pattern, text)

if(matches):
    print(f"Encontró los siguientes valores: {matches}")
    print(f"En total son: {len(matches)}")
else: 
    "No se encontró ningun valor...."


#-------------------------------
### Buscar digito con diagonal invertida y la letra "d", (0-9)

text = "El numero de telefono es 123456789"

found = re.findall(r"\d{9}", text)

print(found)


#-------------------------------
# Ejercicio: Detectar si hay un numero de españa que es el prefijo +34 

text = "Mi numero de telefono es +34 123456789 apuntalo vale?"

pattern = r"\+34 \d{9}"

matches = re.findall(pattern, text)

if(matches):
    print(f"Numero español encontrado: {matches}")
else: 
    print("No")