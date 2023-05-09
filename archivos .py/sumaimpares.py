from functools import reduce

def sumaimparesenrango(n):
    return reduce(lambda x,y:x+y,map(int,[x for x in range(n) if x%2 == 1]))