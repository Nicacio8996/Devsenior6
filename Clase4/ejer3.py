"""
Vamos a calcular el valor a pagar a un empleado por su trabajo de la semana,
le vamos a preguntar al usuario cuantas horas trabajo el empleado y cuanto gana por hora,
y al finalle vamos a mostrar el valor a pagar al empleado por su trabajo de la semana.
"""
nombre = input("Hola, Ingresa el nombre de tu empleado: ")
horas_laboradas = float(input("Hola, Ingresa las horas laboradas de tu empleado: "))
valor_hora = float(input("Hola, ingresa el valor por hora que gana tu empleado:  "))

total_pagar = horas_laboradas * valor_hora
print(f"Hola, hay que pagarle a {nombre} el valor de ${total_pagar:.2f}")

#AGREGUEMOS DOS EMPLEADOS MAS Y CALCULAMOS LA NOMINA DE LA SEMANA
nombre1 = input("Hola, Ingresa el nombre de tu segundo empleado: ")
horas_laboradas1 = float(input("Hola, Ingresa las horas laboradas de tu segundo empleado: "))
valor_hora1 = float(input("Hola, ingresa el valor por hora que gana tu segundo empleado:  "))

total_pagar1 = horas_laboradas1 * valor_hora1
print(f"Hola, hay que pagarle a {nombre1} el valor de ${total_pagar1:.2f}")


nombre2 = input("Hola, Ingresa el nombre de tu tercer empleado: ")
horas_laboradas2 = float(input("Hola, Ingresa las horas laboradas de tu tercer empleado: "))
valor_hora2 = float(input("Hola, ingresa el valor por hora que gana tu tercer empleado:  "))

total_pagar2 = horas_laboradas2 * valor_hora2
print(f"Hola, hay que pagarle a {nombre2} el valor de ${total_pagar2:.2f}")


print("========RESUMEN O TOTAL A PAGAR DE NOMINA==========")
suma = total_pagar + total_pagar1 + total_pagar2
print(f"Hola, deves de pagar un total de ${suma} →🩻")