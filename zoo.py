# Comience creando una clase Animal
class Animal:
    def __init__(self, name, age, health, happiness):
        self.name=name
        self.age=age
        self.health=health
        self.happiness=happiness

# La clase Animal debe tener un método display_info que muestre el nombre, la salud y la felicidad del animal. 
    def display_info(self):
        print(f"Nombre: {self.name}, Edad: {self.age}, Salud: {self.health}, Felicidad: {self.happiness}")
        return self

# Tambien debe tener un metodo de alimentacion que aumente la salud y la felicidad en 10.
    def alimentacion(self):
        self.health += 10
        self.happiness += 10
        return self

# 3 clases específicas de animales que hereden de Animal.
# Cada animal debe tener al menos un nombre, una edad, un nivel de salud y un nivel de felicidad.
class Lion(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)

    def display_info(self):
        super().display_info()
        return self
    
    def alimentacion(self):
        super().alimentacion()
        return self

class Tiger(Animal):
    def __init__(self, name, age, health, happiness):
        super().__init__(name, age, health, happiness)
    
    def display_info(self):
        super().display_info()
        return self
    
    def alimentacion(self):
        super().alimentacion()
        return self

class Penguin(Animal):
    def __init__(self, name, age, health, happiness, habitat):
        super().__init__(name, age, health, happiness, habitat)
    
    def display_info(self):
        super().display_info()
        return self
    
    def alimentacion(self):
        super().alimentacion()
        return self

#instancias probando sin la clase Zoo
#simba=Lion("simba",3,2)
#simba.alimentacion()
#simba.display_info()

#juanito=Penguin("Juanito",4)
#juanito.alimentacion()
#juanito.display_info()

# Clase de zoológico para ayudar a manejar a todos sus animales.
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_lion(self, name, age, health, happiness):
        self.animals.append( Lion(name, age, health, happiness) )
    
    def add_tigger(self, name, age, health, happiness):
        self.animals.append( Tiger(name, age, health, happiness) )
    
    def add_penguin(self, name, age, health, happiness, habitat='Hemisferio sur'):
        self.animals.append( Penguin(name, age, health, happiness, habitat))
    
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()

zoo1 = Zoo("Zoologico")
zoo1.add_lion("Nala", 4, 5, 3)
zoo1.add_lion("Simba", 4, 2, 0)
zoo1.add_tigger("Rajah", 3, 2, 0)
zoo1.add_tigger("Shere Khan", 1, 0 ,0)
zoo1.add_tigger("Juanito", 5, 10 ,9)
zoo1.print_all_info()
