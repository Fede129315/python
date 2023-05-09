import sqlite3

def AgregarRegistro(nombre_Tabla):
    conn = sqlite3.connect('prueba.db')
    cursor = conn.cursor()
    nAlumnos = int(input("Ingrese la cantidad de alumnos: "))
    for arg in range(nAlumnos):
        nombre_apellido = input("Ingrese nombre y apellido: ")
        promedio = input("Ingrese promedio: ")
        query = f'INSERT INTO {nombre_Tabla} VALUES({arg},' \
                f'"{nombre_apellido}",' \
                f'{promedio})'
        print(query)
        cursor.execute(query)
        conn.commit()
    cursor.close()
    conn.close()