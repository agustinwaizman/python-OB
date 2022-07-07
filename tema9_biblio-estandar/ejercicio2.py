from functools import reduce

numeros = input("ingrese los numeros que desee con coma y espacio:\n")

listanum = [num for num in numeros.split(", ")]
listanum2 = []

for i in range(0, len(listanum)):
    nvo = int(listanum[i])
    listanum2.append(nvo)


def ejercicio2(lista):
    resultado = list(filter((lambda x: x % 2), lista))
    print(resultado)
    resultado = reduce((lambda x, y: x + y), resultado)
    print(resultado)

ejercicio2(listanum2)