def mifuncion(nombre="Agustin"):
    print("Hola", nombre)

def suma (a=2, b=5, c=3):
    print(a + b +c)

def suma2 (**kwargs):
    if 'coche' not in kwargs:
        return
    if kwargs['coche'] == 'bonito':
        print('tu coche es bonito')

suma2(coche='feo', color='verde')

def suma3(a, b):
    return a + b

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

res = operaciones(5, 10)


def sumador(**kwargs):
    inicial = kwargs['inicial']
    final = kwargs['final'] if 'final' in kwargs else inicial

    resultado = 0
    for x in range(inicial, final + 1):
        resultado += x
    
    # return resultado
    print(resultado)

sumador(inicial=1, final=5)

anonima = lambda nombre, nombre2: print(f"Holis {nombre}, adios {nombre2}")
anonima("juan", "Agustin")