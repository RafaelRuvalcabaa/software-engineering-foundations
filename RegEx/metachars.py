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

found = re.search(pattern, text)

if (found):
    print(f"Encontré el numero de telefono: {found.group()}")

#-------------------------------
# \w coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

texto = "@@@@@el_rubius_69&%# "

pattern = r"\w"

found = re.findall(pattern, texto)
print(found)


#-------------------------------
### \s: Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)

texto = "Hola mundo\n Como estas? \t"

pattern = r"\s"

matches = re.findall(pattern, texto)

print(matches)


#-------------------------------
### Coincide con el principio de una cadena
# Detectar si un string comienza de una forma. 

username = "@234_name"

pattern = r"^\w" # Validar nombre de usuaurio 

valid = re.search(pattern, username)

if valid:
    print("El nombre de usuario es valido")
else: 
    print(f"{username} no es valido..")



phone = "+343434 2332434435"

pattern = r"\+\d{1,3} "

valid = re.search(pattern, phone)

if valid: 
    print("El numero es valido")
else: 
    print("El numero no es valido")


#-------------------------------
## $: Coincide con el final de una cadena 


text = "Hola, mundo"

pattern = r"mufdfgfgndo$"

valid = re.findall(pattern, text)

if valid: 
    print(f"Se encontró {valid} que es valido.")
else: 
    print(f"No se encontró '{pattern}' en el texto.")



### |: Coincidir con una opcion o otra

fruits = "platano, manzana, aguacate, pera, palta"

pattern = r"manzana|p..a|\b\w{7}\b"

found = re.findall(pattern, fruits)

print(found)


###-----------------------------
#### Genera una regex para encontrar las palabras man fan y ban pero ignore el resto. 

text = "man ran fan pan jan kan ñan ban onmiman"

pattern = r"[mfb]an"

found = re.findall(pattern,text)

if found: 
    print(found)
else: 
    print("No se encontró ningun patrón...")



###-----------------------------
#### Genera una regex para encontrar las palabras man fan y ban pero ignore el resto.
# ------------------------------
# Lo mismo pero que limite por ejemplo "onmiman" porque en el ejemplo anterior las pasa 

text = "man ran fan pan jan kan ñan ban onmiman"

pattern = r"[mfb]an\b"

found = re.findall(pattern,text)

if found: 
    print(found)
else: 
    print("No se encontró ningun patrón...")



###-----------------------------
#### Genera una regex para encontrar los numeros del 1 al 2 solamente
#------------------------------


text = "22"

pattern = r"[1-2]"

found = re.findall(pattern,text)
 
print(found)


###-----------------------------
# Ejercicio final: 
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner case y arreglarlo: 

"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# []: coincide con cualquier caracter dentro de los corchetes

text = "Hola mundo"

pattern = r"[^aeiou]"

found = re.findall(pattern, text)

print(found)