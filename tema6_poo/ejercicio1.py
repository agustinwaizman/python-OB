class Vehiculo:
    color = "Negro"
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

auto = Coche()
auto.cilindrada = 1500
auto.velocidad = 240
auto.ruedas = 4
auto.puertas = 5
print(f"Mi auto tiene una cilindrada de {auto.cilindrada}, la velocidad maxima es de {auto.velocidad}km/h, tambien tiene {auto.ruedas} ruedas y {auto.puertas} puertas")