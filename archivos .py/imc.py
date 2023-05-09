def imc():
    peso = float(input("Ingrese su peso en kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    return round(peso/estatura ** 2,2)
