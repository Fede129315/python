import sqlite3

def CreaTabla(nombre_Tabla):
    nCol = int(input("Ingrese el número de Headers sin contar el id: "))
    Listaheaders = []
    Listatypes = []
    for arg in range(nCol):
        Listaheaders.append(input(f"Ingrese el header del la columna {arg}: "))
        Listatypes.append(input(f"Ingrese el type del la columna {Listaheaders[arg]}: "))
    conn = sqlite3.connect('prueba.db')
    cursor = conn.cursor()
    query2=""
    for arg in range(nCol):
       if arg == nCol - 1:
           query2 = query2 + f'{Listaheaders[arg]} {Listatypes[arg]} NOT NULL'
       else:
           query2 = query2 + f'{Listaheaders[arg]} {Listatypes[arg]} NOT NULL,'
    query = f'CREATE TABLE IF NOT EXISTS {nombre_Tabla}(id INTEGER PRIMARY KEY ,'+query2+");"
    cursor.execute(query)
    cursor.close()
    conn.close()
