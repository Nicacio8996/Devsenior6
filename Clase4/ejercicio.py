"""
Ejercico paractico.
Mini script de calculadora basica que pidada datos,
procese operaciones y entregue resulatdos formateados profecinalmente.
"""
#Hola Adriano la suma d elos numeros es:
#La resta d e los numeros es:
#La multiplicacion de los numeros es:
#La divicicon de los numeros es:
#La divicion entera de los numeros es:
#El modulo de la divicion de los numeros es:
#La potencia de los numeros es:
nombre = input("Ingrese su nombre comlpeto: ")
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))

suma = numero1 + numero2
print(f"Hola {nombre} la suma de los numeros es {suma}")

multiplicacion = numero1 * numero2
print(f"Hola {nombre} la multiplicacion de los nuemros es {multiplicacion}")

resta = numero1 - numero2
print(f"Hola {nombre} la resta de los numeros es {resta}")

divicion = numero1 / numero2
if numero2 == 0:
    print(f"Hola {nombre} no se puede dividir por cero")
else:
    print(f"Hola {nombre} la divicion de los numeros es {divicion}") 

divicion_entera = numero1 // numero2
print(f"Hola {nombre} la divicion entera es {divicion_entera}")

potencia1 = numero1**numero2
potencia2 = numero2**numero1
print(f"Hola {nombre} la potencia de los numaros es {potencia1}")
print(f"Pero mira {nombre} la potencia al reves seria {potencia2}")

modulo = numero1 % numero2
print(f"Hola {nombre} el modulo de los numeros es {modulo}")
