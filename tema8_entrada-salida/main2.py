import pickle

class Juguete:
    nombre = ''
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

# j1 = Juguete('dinosaurio', 10)
# f = open('datos.bin', 'wb')
# pickle.dump(j1, f)
# f.close()

f = open('datos.bin', 'rb')
dinosaurio = pickle.load(f)
f.close()

print(type(dinosaurio))
print(dinosaurio.getNombre(), 'precio: ', dinosaurio.precio)

class Estado:
    players = Players()
    status = Status()
    life_remaining = 12
    armor = False

f = open('gamestatus.dat', 'wb')
e = Estado()
pickle.dumps(f, e)
f.close()