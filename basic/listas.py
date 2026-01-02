


def pali(arr):

    largo = len(arr)
    for i in range (len(arr)):
            if arr[i] != arr[largo-1-i]:
                return False
            else: 
                return True 
            


print(pali("oso"))


def otra(arr):
    if arr == arr[::-1]:
        return True
    else:
        return False

print(otra("Rafa"))


lista = [1,2,3,4,5,6]

print(lista[0:3])