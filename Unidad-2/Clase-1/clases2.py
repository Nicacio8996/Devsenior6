class Persona:
    def __init__(self, nombre):# Metodos → Cracteristicas
        self.__nombre = nombre #Esto es encapsulamiento porque esta privado

#mancito = Persona("Adriano")
#print (mancito.__nombre) #Esto genera un error por que le atributo esta privado

    def get__nombre(self):# Atributos → Acciones
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    

persona1 = Persona("Adriano") #Este ya seria un objeto
#print(persona1.nombre) # sale error por que esta privado se utilza get
print(persona1.get__nombre())# sale: → Adriano

persona1.set_nombre("Carlos")
print(persona1.get__nombre())

p1 = Persona("Maria")
print(p1.get__nombre())  #Salida Maria
  

# Getters y Setters → get, set → Son metodos que se utilzan para acceder
# y modificar los atributos privados de una clase. 