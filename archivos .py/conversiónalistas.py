def converlista():
    """
    estos dos bloques de codigo representan lo mismo el segundo se llama listas de comprensión y son más rapidos
    """
    lista = []
    for i in range(11):
        lista.append(i)

    lista2 = [i for i in range(11)]
    lista3 = [i for i in range(-10,1,1)]
    lista4 = [i for i in range(22) if i%2 == 0]
    lista5 = [i for i in range(-20,1,1) if i%2 == 1]
    lista6 = [i for i in range(51) if i % 5 == 0]

    return list(lista), list(lista2), list(lista3), list(lista4), list(lista5), list(lista6)