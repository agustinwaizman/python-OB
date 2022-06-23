numero_inicial = int(input("ingrese el numero inicial: "))
numero_final = int(input("ingrese el numero final: "))

for i in range(numero_inicial, numero_final):
    if (i % 2) == 1:
        print(i)
