import validanombre as v
import validacontraseña as c


def validausuycontra():
    v.validanombre(input("Ingrese el nombre de usuario: "))
    c.validacontrasena(input("Ingrese la contrasena: "))
