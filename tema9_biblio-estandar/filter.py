numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mifuncion(x):
    if str(x).startswith("n"):
        return True
    return False

resultado = filter(mifuncion, ["numeros", "numeritos", "pepe"])
print(list(resultado))
