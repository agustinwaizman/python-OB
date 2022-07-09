import sqlite3

def crear_alumno(id, nombre, apellido):
    cursor.execute(f'INSERT INTO Alumnos VALUES({id}, "{nombre}", "{apellido}")')
    conn.commit()

def buscar_alumno(nombre):
    cursor.execute(f"SELECT * FROM Alumnos WHERE Nombre = '{nombre}'")
    fila = cursor.fetchall()
    print(fila)

conn = sqlite3.connect('datos_alumnos.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

crear_alumno(1, "Agustin", "Waizman")
crear_alumno(2, "Micaela", "Monteporcci")
crear_alumno(3, "Lucas", "Facal")
crear_alumno(4, "Miguel", "Martinez")
crear_alumno(5, "Lautaro", "Medina")
crear_alumno(6, "Matias", "Ifran")
crear_alumno(7, "Gabriel", "Torres")
crear_alumno(8, "Nestor", "Miño")
crear_alumno(9, "Ulises", "Romero")

buscar_alumno("Agustin")

cursor.close()
conn.close()
