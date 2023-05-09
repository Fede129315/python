import time
from datetime import datetime

def enhorariolaboral():
    ingreso = datetime.strptime(input("ingrese el horario de ingreso: "), '%H')
    egreso = datetime.strptime(input("ingrese el horario de ingreso: "), '%H')
    if int(datetime.strftime(ingreso, '%H')) > time.localtime().tm_hour < int(datetime.strftime(egreso, '%H')):
        return "En horario laboral, quedan: ",time.localtime().tm_hour-int(datetime.strftime(ingreso, '%H')),"hs para irse"
    elif int(datetime.strftime(ingreso, '%H')) == time.localtime().tm_hour:
        return "Hora de entrar"
    elif int(datetime.strftime(egreso, '%H')) == time.localtime().tm_hour:
        return "Hora de irse"
    elif int(datetime.strftime(ingreso, '%H')) > time.localtime().tm_hour:
        return "Aun no es hora, quedan: ",int(datetime.strftime(ingreso, '%H')) - time.localtime().tm_hour, "hs para el ingreso"
    elif int(datetime.strftime(egreso, '%H')) < time.localtime().tm_hour:
        return "Te pasaste: ",time.localtime().tm_hour - int(datetime.strftime(egreso, '%H')) , "hs del horario de salida"






