import re

target = "IA"

text = "La inteligencia artificial avanza rápidamente y se integra en múltiples áreas de la vida diaria, desde la automatización hasta el análisis de datos complejos. En medio de este desarrollo, IA aparece como un concepto clave que redefine la forma en que interactuamos con la tecnología."


found_AI = re.search(target, text)

if found_AI: 
    print(f"He encontrado el patrón en la posicion {found_AI.start()} y termina en la posicion {found_AI.end()}")
else: 
    print("No lo he encontrado")

