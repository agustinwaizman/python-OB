class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

name = input("Ingrese el nombre del alumno: ")
note = int(input("ingrese la nota: "))

a = Alumno(name, note)

if a.nota >= 6:
    print(f"Felicidades, el alumno {a.nombre} ha aprobado con un {a.nota}")
else: print(f"lamentablemente el alumno {a.nombre} ha desaprobado con una nota de {a.nota}")

