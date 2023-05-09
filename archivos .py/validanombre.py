def validanombre(nombre):
    valido = False
    while valido == False:
        if 12 >= len(nombre) >= 6 and nombre.isalnum():
            valido = True
            print(nombre.isalnum())
        elif len(nombre) < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
            nombre = input("Ingrese el nombre de usuario: ")
        elif len(nombre) > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
            nombre = input("Ingrese el nombre de usuario: ")
        elif nombre.isalnum() == False:
            print("El nombre de usuario puede contener solo letras y números")
            nombre = input("Ingrese el nombre de usuario: ")
        else:
            print("Intente nuevamente")
            nombre = input("Ingrese el nombre de usuario: ")

    return valido