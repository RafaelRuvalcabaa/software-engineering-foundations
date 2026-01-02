
# for i in frutas:
#     print(i) 


# cadena = "rafael"
# for caracter in cadena:
#     print (caracter)


# enumerate 

# frutas = ["manzana", "pera", "mandarina", "limon"]

# for idx, fruta in enumerate(frutas):
#     print(f"El indice es {idx} y la fruta es {fruta}")

# letras = ["A","B","C"]

# numeros = [1,2,3]

# for letra in letras:
#     for numero in numeros: 
#         print(f"{letra}{numero}")


animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for idx, animal in enumerate(animales):
    if animal == "loro":
        # print(f"El loro se encuentra en la posición {idx}")
        # break; 
        continue
    print(animal)


# Compresion de listas (list comprehesion)

animales_mayus = [animal.upper() for animal in animales]

print(animales_mayus)


#Muestra los numeros pares de una lista 

pares = [num for num in [1,2,3,4,5,6,7,8,9] if num % 2 == 0]

print(pares)


