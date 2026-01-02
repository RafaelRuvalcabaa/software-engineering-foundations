
import os 
os.system("cls")


#Pedirle al usuario un número que tiene que ser positivo si no, no le dejamos en paz....

# numero = -1 

# while numero <=0:
#     numero = int(input("Escribe un numero positivo: "))
#     if numero < 0: 
#         print("Intenta de nuevo..")
# print(f"El numero introducido y correcto es: {numero}")     


# numero = -1 

# while numero <=0:
#     try:
#         numero = int(input("Escribe un numero positivo: "))
#         if numero < 0: 
#             print("Intenta de nuevo.....")
#     except: 
#         print("Lo que introduces dede ser un numero")

# print(f"El numero introducido y correcto es: {numero}")     


def facto(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *= i 
    return resultado

print(facto(10))

