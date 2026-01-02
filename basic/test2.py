# Cambiar el primer y ultimo indice 

lista = [1,2,3,4,5]
print(f"Lista original: {lista}")

# Intercambio = lista[1]
intercambio = lista[0]
# Lista[1] = lista[5] 
lista[0] = lista[-1]
# Lista[5] = intercambio[1]
lista[-1] = intercambio 




print(f"Lista cambiada con el primer y el ultimo indice {lista }")