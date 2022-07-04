from operator import truediv
import this


class Dino:
    _encendido = True
    def apaga(self):
        self._encendido = False
    def enciende(self):
        self._encendido = True

d = Dino()

# class Estatica:
#     numero = 0

#     def incrementa():
#         Estatica.numero += 1

# Estatica.incrementa()
# print(Estatica.numero)

# Estatica.incrementa()
# print(Estatica.numero)

class Juguete:
    _encendido = True
    def __init__(self):
        pass
    def enciende(self):
        print("Prendiendo...")
        self._encendido = True
    def apaga(self):
        print("Apagando...")
        self._encendido = False
    def estaEncendido(self):
        return self._encendido

# class Caradepapa(Juguete):
#     _tieneOreja = True
#     def sacarOreja(self):
#         print("Sacando...")
#         self._tieneOreja = False
#     def ponerOreja(self):
#         print("Colocando...")
#         self._tieneOreja = True

class Dinosaurio(Juguete):
    _escamas = True
    color = None
    nombre = ""
    def __init__(self, nombre, color):
        super().__init__()
        self.nombre = nombre
        self.color = color

    def tieneEscamas(self):
        return self._escamas

# señor = Caradepapa()
# señor.enciende()
# print(señor.estaEncendido())
# señor.apaga()
# print(señor.estaEncendido())
# señor.sacarOreja()
# señor.ponerOreja()

p = Dinosaurio("Tiranosaurio Rex", "Rojo")
print(p.nombre)
print(p.color)

# _encendido = False
# def enciende():
#     global _encendido
#     _encendido = True
# def apaga():
#     global _encendido
#     _encendido = False
# def isEncendido():
#     return _encendido

# diccionario = {
#     '_encendido': False,
#     'enciende': enciende,
#     'apaga': apaga,
# }
# diccionario['enciende']()

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass
    def deciHola(self):
        print("hola")
# no se pueden instanciar sin derivar

class Perro(Animal):
    def sonido(self):
        print("Wau")
class Gato(Animal):
    def sonido(self):
        print("Miau")

p = Perro()
p.sonido()
p.deciHola()

g = Gato()
g.sonido()
p.deciHola()