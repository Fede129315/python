def validacontrasena(contrasena):
    valido = False
    while valido == False:
        if len(contrasena) >= 8:
            if any(caracter.isdigit() for caracter in contrasena):
                if any(caracter.islower() for caracter in contrasena):
                    if any(caracter.isupper() for caracter in contrasena):
                        if all(caracter.isalpha() for caracter in contrasena) == False:
                            if any(caracter.isspace() for caracter in contrasena) == False:
                                valido = True
        if valido == True:
            return valido
        else:
            return "La contraseña elegida no es segura"