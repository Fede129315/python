def bisiesto():
    anio = int(input("Ingrese el anio: "))
    if (anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0)):
        return "Es bisiesto"
    else:
        return "No es bisiesto"
