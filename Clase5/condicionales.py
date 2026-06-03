# Vamos a hacer un programa que nos diga el sueldo a recibir de un empleando,
# si gana menos de dos  millones de pesos le vamos a dar un subsidio de 200000$
sueldo = float(input("Ingrese el sueldo del empleado: "))
if sueldo < 2000000:
    print("Si se cumplio la condicón")
    sueldo += 200000
else:
    print("No se cumplio la condición")
print("El sueldo del empleado es: ", sueldo)
"""
a = 100
print(a > 50)
print(a + 50)
"""

