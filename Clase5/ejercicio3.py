"""
Escribir un programa en Python que solicite al usuario un numero entre 1 y 7

si es 1 imprimir "Lunes"
si es 2 imprimir "Martes"
si es 3 imprimir "Miercoles"
si es 4 imprimir "Jueves"
si es 5 imprimir "Viernes"
si es 6 imprimir "Sbado"
si es 7 imprimir "Domingo"

Y si el numero no esta entre  1 y 7 imprimir "Numero no valido"

"""


numero = int(input("Ingresa un numero que este entre 1 y 7: "))
if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")
else:
    print("Numero no valido")

#=============================================#
# Otra manera para el mismo funcinamiento.
dia = int(input("Ingresa un numero que este entre 1 y 7: "))
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _: #Hace la funcion del else:
        print("Numero no valido")

#=============================================#
# Otra manera para el mismo funcinamiento pero con cadena de texto o caracteres.
dia = input("Ingresa un numero que este entre 1 y 7: ")
match dia:
    case "1":
        print("Lunes")
    case "2":
        print("Martes")
    case "3":
        print("Miercoles")
    case "4":
        print("Jueves")
    case "5":
        print("Viernes")
    case "6":
        print("Sabado")
    case "7":
        print("Domingo")
    case _: #Hace la funcion del else:
        print("Numero no valido")