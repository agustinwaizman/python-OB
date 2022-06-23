# if condicion:
# acciones

# a = 5
# b = 6
# resultado = (a < b)
# print(resultado)

# contador = 1

# while contador <= 10:
#     print("contador vale", contador)
#     # if contador == 5:
#     #     break
#     if contador % 2 == 0:
#         print(contador, "es un numero par")
#     print("incrementa el contador")
#     contador += 1

# print("while finalizado")

# lista = [1, 2, 3, "sisoy", 5]

# for i in lista:
#     print(i)

# for i in range(5, 11000000):
#     print(i)

# longitud = len(lista)

# for i in range(longitud):
#     print(lista[i])

palabra = str(input("ingrese la palabra que desee buscar: "))
lista = ["hola", "mensaje", "chau"]

for i in lista:
    if i == palabra:
        print(f"palabra {palabra} encontrada!")
        break
else:
    print(f"no se encuentra la palabra {palabra}")

# for palabra in lista:
#     print("palabra actual:", palabra)
#     if palabra == "mensaje":
#         print(f"se ha encontrado la palabra {palabra}")
#         break
#     else: print("No es la palabra solicitada")

# if "mensaje" in lista:
    # print("se ha encontrado la palabra")



# lista = [3, 5, 4, 7, 6]
# print(lista)

# listaOrdenada = sorted(lista)
# listaReverse = sorted(lista, reverse = True)
# print(listaOrdenada)
# print(listaReverse)

# valor = 1

# if valor == 1:
#     print("valor es 1")
# elif valor == 2:
#     print("valor es 2")
# elif valor == 3:
#     print("valor es 3")
# elif valor == 4:
#     print("valor es 4")
# elif valor == 5:
#     print("valor es 5")
# elif valor == 6:
#     print("valor es 6")

# match valor:
#     case 1:
#         print(f"valor es {valor}")
#     case 2:
#         print(f"valor es {valor}")
#     case 3:
#         print(f"valor es {valor}")
#     case 4:
#         print(f"valor es {valor}")
#     case 5:
#         print(f"valor es {valor}")
#     case 6:
#         print(f"valor es {valor}")