"""
Preguntar al ususario un animal(Perro, Gato, pez)
Si el animal es perro imprimir "Guau"
Si el animal es pez Imprimir "Blub"
Si el animal es gato imprimir "Miau"

Y si el animal no es ninguno de esos imprimir "Animal no reconocido"
"""
animal = input("Ingrese el nombre de un anima: 'Perro' 'Pez', o 'Gato': →  ").title()
match animal:
    case "Perro":
        print("El perro Hace guauu")
    case "Pez":
        print("El pez Hace Blub")
    case "Gato":
        print("El Gato Hace Miau")
    case _:
        print("Animal No reconocido")
