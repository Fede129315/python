from functools import reduce
"""
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
"""
def impares(numeros):
    return reduce(lambda x,y:x+y ,filter(lambda n : n%2 == 1, map(int,numeros.split())))