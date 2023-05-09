def suma(*args):
    print("Suma")
    n = 0
    for arg in args:
        n += arg
    return n

def resta(*args):
    print("Resta, Al primer numero se le restan los siguientes")
    n = args[0]
    for arg in args:
        n -= arg
    return n


def multiplica(*args):
    print("Multiplica")
    n = 1
    for arg in args:
        n *= arg
    return n


def divide(a, b):
    print("Divide")
    return a/b


