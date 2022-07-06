from pickle import *

class Vehiculo:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
    def __str__(self):
        return self.color + ' ' + self.puertas

gol = Vehiculo("Negro", "3")
print(gol)

file = open('vehiculo_objeto', 'w+b')
dump(gol, file)

file.seek(0)
nuevo_gol = load(file)

print(nuevo_gol)
file.close()