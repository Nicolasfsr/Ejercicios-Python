""""
# Character input
Cree un programa que le pida al usuario que ingrese su nombre y su edad. Imprime un mensaje dirigido a ellos que les indique el año en que cumplirán 100 años. Nota: para este ejercicio, la expectativa es que escriba explícitamente el año (y, por lo tanto, esté desactualizado el próximo año). Si quiere hacer esto de forma genérica, vea el ejercicio 39.

##Extras:
* Agregue al programa anterior pidiéndole al usuario otro número e imprimiendo tantas copias del mensaje anterior. ( Pista: el orden de las operaciones existe en Python )
* Imprima esa cantidad de copias del mensaje anterior en líneas separadas. ( Pista: la cadena "\nes lo mismo que presionar el botón ENTER )

#+1000
"""

nombre = input("Escriba su nombre: \n")
edad = int(input("Escriba su edad: \n"))
cant = int(input("Escriba la cantidad de veces que se imprima \n"))
año = 2022
acen = año - edad + 100
for i in range(cant):
  print("Usted", nombre,  "cumplira cien años en", acen)