numero_inicial = int(input("ingrese el numero inicial: "))
numero_final = int(input("ingrese el numero final: "))
numeros_impares: [int] = []

for i in range(numero_inicial, numero_final):
    if (i % 2) != 0:
        numeros_impares.append(i)
print(f"esta es la lista de numeros impares entre {numero_inicial} y {numero_final}:")
print(numeros_impares)
