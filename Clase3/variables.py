#QUE ES UNA VARIABLE?
"""
Es un espacio en memoria en le cual guardo información
en donde guardo un dato, es como una cajita donde guardo cosas que estoy utulizando.
"""
# = → Para asignar por ejemplo un numero auna edad; → edad = 38
# = → podemos guardar un string → nombre = 'Adriano'
edad = 38
nombre   = 'Adriano'

# PODEMOS GUARDAR VARIOS TIPOS DE DATOS.
edad = 38 # → enteros → int → numericos
PI = 3.1416 # → float → decimales
nombre = "Adriano figueroa" # → Caracteres o cadenas de texto → string
casado = False # ESte un boolean → Falso o Verdadero (False/True)

print(type(edad))
print(type(PI))
print(type(nombre))
print(type(casado))
PI = "Pajarito" # → esto es tiádo dinamico → Durante de la ejecucion puede cambiar
print(type(PI))

largo = 5
ancho = 3
area = largo * ancho
print("El area del rectandulo es:", area)


