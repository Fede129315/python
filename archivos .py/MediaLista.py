
def medialista(cant):
    lista = []
    num = 0
    for i in range(cant):
        num = float(input("Ingrese numero  "))
        lista.append(num)

    return sum(lista)/len(lista)