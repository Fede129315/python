"""
Utilizar la función incorporada map() para crear una función que retorne
una lista con la longitud de cada palabra (separas por espacios) de una frase.
La función recibe una cadena de texto y retornara una lista.
"""
def longitudpalabras(frase):
    separadasporespacios = list(map(len,frase.split()))
    return separadasporespacios