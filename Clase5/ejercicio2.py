"""
1. de cero a 5 primera infancia.
2. de 6 a 12 infancia.
3. de 13 a 17 adolecencia.
4. mayos a 18 adultes.
"""
edades = int(input("Ingrese su edad: → 🤺 "))
if edades >= 0 and edades <= 5:
    print("Estas en al primera infancia. ")
elif edades >= 5 and edades  <= 12:
    print("Estas en tu inafancia: → 🩻")
elif edades >= 13 and edades <= 17:
    print("Estas en la adolecencia: 🚘 ")
else:
    print("Y eres adulto: 😱")

#========================================#
#Otr codigo misma funcion
edad = int(input("Ingrese su edad: → 🤺 "))
if edad < 0:
    print("Edad no valida: ")
elif edad <= 5:
    print("Primera infancia:")
elif edad <= 12:
    print("Infancia")
elif edad <= 17:
    print("Adolecencia:")
else:
    print("Adultez")
