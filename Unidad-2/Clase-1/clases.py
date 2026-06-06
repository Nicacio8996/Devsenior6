class Perro: #Clase perro
    def __init__(self, nombre, edad):# Atributos → Caracteristica → pueden ser (+PUBLICOS, #PROTEGIDOS, -PRIVADOS)
        self.nombre = nombre
        self.edad = edad
    
    def ladrar(self): # Metodos → Acciones
        return "¡Guauu!"
    
    def rascarse(self):
        print("¡Me estoy rascando!")
    
perro1 = Perro("Fido", 3)
perrito = Perro("Trosky", 5)
print(f"El perro se llama {perro1.nombre}, tiene {perro1.edad} años de edad")
print("Y hace", perro1.ladrar())
print(f"El perrito se llama {perrito.nombre}, tiene {perrito.edad} años de edad")
print(f"Y hace {perrito.ladrar()}")
perro1.rascarse()
perrito.rascarse()
