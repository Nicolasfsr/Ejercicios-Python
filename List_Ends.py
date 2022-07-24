"""
#List Ends
Escriba un programa que tome una lista de números (por ejemplo, a = [5, 10, 15, 20, 25])y haga una nueva lista de solo
el primer y último elemento de la lista dada. Para practicar, escribe este código dentro de una función.

"""
a = [5, 10, 15, 20, 25, 67]
n = []
def Listas(lista):
    lon = len(lista)
    lon = lon-1
    n.append(lista[0])
    n.append(lista[lon])
Listas(a)
print(n)