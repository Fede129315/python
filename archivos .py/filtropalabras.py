"""
Crear una función que retorne las palabras de una lista de palabras
 que comience con una letra en especifico. Utilizar la función filter.
"""
def filtropalabras(frase,letra):
    return list(filter(lambda palabra:palabra[0] == letra, frase.split()))

"""
la funcion lambda 
Sintaxis de una función Lambda
lambda argumentos: expresión

Las funciones Lambda pueden tener cualquier número de argumentos, pero solo una expresión.

Código de ejemplo:

# Función Lambda para calcular el cuadrado de un número
square = lambda x: x ** 2
print(square(3)) # Resultado: 9
"""