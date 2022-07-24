"""
Max of three

Implemente una función que tome como entrada tres variables y devuelva la mayor de lastres. ¡Haz esto sin usar la 
función de Python max()!
El objetivo de este ejercicio es pensar en algunas partes internas que Python normalmente se ocupa de nosotros. 
¡Todo lo que necesita son algunas variables y if declaraciones!
"""
a = int(input("Ingrese el primer numero: \n"))
b = int(input("Ingrese el segundo numero: \n"))
c = int(input("Ingrese el tercer numero: \n"))
max = 0
if a > b and a > c:
    max = a
    print("El mayor de los numeros es",max)
elif b > a and b > c:
    max = b
    print("El mayor de los numeros es",max)
elif c > b and c > a:
    max = c
    print("El mayor de los numeros es",max)
elif a == b and b == c and c == a:
    print("Ningun numero es mayor")
elif a == b:
    print("El mayor de los numeros es", a)
elif a == c:
    print("El mayor de los numeros es", c)
elif c == b:
    print("El mayor de los numeros es", b)