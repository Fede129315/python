import sqlite3

def BorrarTabla(nombre_Tabla):
    conn = sqlite3.connect('prueba.db')
    cursor = conn.cursor()
    cursor.execute(f'DROP TABLE {nombre_Tabla}')
    cursor.close()
    conn.close()
