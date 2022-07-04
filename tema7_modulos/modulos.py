# from pprint import pprint
# import operaciones.suma

# def main():
#     pprint(dir())
#     mp = operaciones.suma.Multiplicador()
#     print(mp.multiplicacion(3, 5))
#     res = operaciones.suma.suma(2, 5)
#     print("hola", res)

# main()

from pprint import pprint


# variable = 5
# print(variable)

# globals()['variable'] = 6
# print(variable)

# def prueba():
#     globals()['variable'] = 6

# prueba()
# print(variable)

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

def prueba(inicial):
    valor = 5
    estado = False
    pprint(locals())

prueba(2)
pprint(globals())