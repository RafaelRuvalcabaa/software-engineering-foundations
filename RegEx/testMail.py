## Ejercicio 
### Valida que una correo sea de gmail 

import re

text = "callme@gmail.com"

pattern = r"^\w+@gmail\.com$"

valid = re.search(pattern, text)

if valid:
    print(f"El correo: {text} es válido")
else:
    print("No es válido..")
