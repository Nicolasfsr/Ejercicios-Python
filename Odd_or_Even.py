"""
#Odd Or Even
El ejercicio viene primero (con algunos extras si desea un desafío adicional o quiere pasar más tiempo), seguido de una discusión. ¡Disfrutar!

Pide al usuario un número. Dependiendo de si el número es par o impar, imprima un mensaje apropiado para el usuario. Pista: ¿cómo reacciona de manera diferente un número par/impar cuando se divide por 2?

##Extras:

* Si el número es un múltiplo de 4, imprima un mensaje diferente.
* Solicite al usuario dos números: un número para verificar (llámelo num) y un número para dividir por ( check). Si se checkdivide uniformemente en num, dígaselo al usuario. Si no, imprima un mensaje apropiado diferente
"""

num = int(input("Ingrese un numero: \n"))
nume = num % 2
four = num % 4
if num == 0:
  print("El numero es 0")
elif four == 0:
  print("El numero es multiplo de cuatro")
elif nume == 0:
  print("El numero es Par")
else:   
  print("El numero es Impar")
check = int(input("Ingrese un numero para dividir: \n"))
if check == 0 or num == 0:
  print("No se puede dividir entre 0")
else:
  resul = num%check
  if resul == 0:
    print("El numero", num, "es divisible entre" ,check)
  else:
    print("El numero", num, "no es divisible entre" ,check)