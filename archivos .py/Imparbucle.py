"""
Escribir un programa que pida al usuario cuántos números
quiere introducir. Luego que lea todos los números y realice
una media aritmética.

"""
def impar(n):
    while n % 2 != 1:
        n = int(input("ingrese número impar: "))

    return "El número es impar"