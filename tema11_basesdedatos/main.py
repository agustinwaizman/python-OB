import sqlite3
import getpass

def main():
    crear_usuario(4, "Pepe", "abc123")

def main2():
    username = input('username: ')
    password = getpass.getpass('password: ')
    if verifica_credenciales(username, password):
        print('login correcto')
    else:
        print('login incorrecto')

def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f'SELECT id FROM users WHERE username="{username}" AND password="{password}"'
    print("Query a ejecutar: ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    cursor.close()
    conn.close()

def crear_usuario(id, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f'INSERT INTO users(id, username, password) VALUES({id}, "{usuario}", "{clave}"'
    rows = cursor.execute(query)
    print(type(rows))
    conn.commit()  
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main2()

conn = sqlite3.connect('miaplicacion.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM users WHERE username="Pepe"')
for row in rows:
    print(row)

cursor.close()
conn.close()