import sqlite3

def busquedafiltro(nombreTabla,nombreColumna,nombreFiltro):
    conn = sqlite3.connect('prueba.db')
    cursor = conn.cursor()
    query = f'SELECT * FROM {nombreTabla} ' \
            f'WHERE {nombreColumna} = {nombreFiltro}'
    rows = cursor.execute(query)
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
