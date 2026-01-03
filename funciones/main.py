#Funciones - Bloques de codigo 


def saludar():
    print("Hola")

saludar()


def saludar_a(name):
    print(f"!Saludos a {name} ....")


saludar_a("Rafa")



def sumar(x,y):
    total = x+y
    return total;

print(sumar(2,5))


#Documentar funciones con docstring 

def restar (a,b):
    """Restar dos numeros y devuelve el resultado""" 
    return a-b 


print(restar(3,1))

print(restar.__doc__)

help(restar)


#Parámetro por defecto 

def multiplicar (a,b=2):
    return a+b 
"""funcion de sumar pero con un valor por defecto en b, si tu pones un numero en B se sustutuye"""
print(multiplicar(2))


#Argumentos por clave 

def describir_persona(nombre,edad,sexo):
    print(f"Soy {nombre}, tengo {edad} y me identifico como {sexo}")


#los parametros son posicionales 

describir_persona("Rafael", 25, "Masculino")
describir_persona("Gato", 22, "Rafael")

#Argumentos por clave 
#Paramentros nombrados
#Aqui no interfiere la posicion, con el nombramiento de asigna a la variable
describir_persona(sexo="gato", nombre = "Midudev", edad=25)
    

#Argumentos de longitud de varible 

def sumarNum(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma
    


print(sumarNum(1,2,5,7,53,6,8,6,3,1))



# Argumnentos de clave-valor variable (**kwargs)

def mostrar_informacion_de(**kwargs)


