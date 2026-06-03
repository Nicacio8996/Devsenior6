"""
Reforzar la comprencion profunda de tipos y operaciones.
Promover el uso profecional de nombres, comentarios y estructuras.
Imprecion con formato.
"""
#Imprecion sin formato.
print("Hola Mundo", 5 + 2, "Esto es una suma:")


#Imprecion con formato
print(f"Hola Mundo {5 + 2} esto es una suma:")

print("Hola Mundo {} esto es una suma:".format(5 + 2))

#Reenplazando por el contenido de una variable.
a = 5
b = 2
suma = a + b
print("Hola Mundo", suma, "Esto es una suma:")
print(f"Hola Mundo {suma} Esto es una suma:")
print("Hola Mundo {} Esto es una suma:".format(suma))

#Asignación a variables Multiple.
a, b ,c = 1, 2, 3
print(f"Los valores son a={a}, b={b}, c={c}")

# A varias variables le asigno el mismo valor
n1 = n2 = n3 = 5
print(f"Los valores son n1 = {n1}, n2 = {n2}, n3 = {n3}")

#=======================================================#
edad1 = 25
edad2 = 30
nombre1 = "Adriano"
nombre2 = "Maria"
print("La edad de", nombre1, "es",edad1, " y la edad de ",nombre2, " Es",edad2)
print(f"La edad de {nombre1} es {edad1} y la edad de {nombre2} es {edad2}")

#=============================================================================#
edad1 = 25
edad2 = 30
nombre1 = "Adriano"
nombre2 = "Maria"
print(edad1 + edad2)
print(nombre1 + nombre2 + str(edad1 + edad2)) # se combierte en string para poder usar las edades coo texto.

#===========================================================================================#
"""
Programa que le pregunta el nombre y la edad y te saluda
"""
nombre1 = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("Hola " + nombre1 + ", tienes " + edad + " años de edad:") #Linea concatenada.
#No se puede concatenar numeros con cadena de caractres.
#=================================================================#
#Foramtear profecinalmente


