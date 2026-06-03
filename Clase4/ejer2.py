#Escribir un programa que calcule el area de un circulo.
nombre = input("Ingresa tu nombre: ")
numero = float(input("Ingrese el radio del circulo, y te saco el area: "))
area = 3.1416 * numero**2
print(f"Hola {nombre.title()} el area de tu circulo de acuerdo a tu radio es: {area:.2f}")

#Area de un triangulo rectangulo
base = float(input("Ingrese la base de triangulo rectangulo: "))
altura = float(input("Ingrese la altura del triangulo rectangulo: "))
area = (base * altura) / 2
print(f"El area de tu triangulo es: {area:.2f}")