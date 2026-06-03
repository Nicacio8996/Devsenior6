"""
Escribir un programa en python que le solicite al usuario su edad
y que determine si es mayor de edad o no.
si la edad es mayor  o igual a 18 años, el programa debe de imprimir,
"Eres mayor de edad" en caso contrario "Eres menor de edad"
"""
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad: 😎 ")
else:
    print("Eres menor de edad: 😞")