class Motor:
    tipo = "Naftero"

class Ventanas:
    cantidad = 5
    def cambiarCantidad(self, valor):
        self.cantidad = valor

class Ruedas:
    cantidad = 4

class Chasis:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Auto:
    motor = Motor()
    chasis = Chasis()

c = Auto()
print(f"el motor es {c.motor.tipo}")
c.chasis.ventanas.cambiarCantidad(3)
print(f"tiene {c.chasis.ventanas.cantidad} ventanas")
print(f"tambien tiene {c.chasis.ruedas.cantidad} ruedas")

for i in range(1, 1000100000000000):
    i += i
    print(i)