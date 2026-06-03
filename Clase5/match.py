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