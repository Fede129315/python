class archivoSalida:
    def __init__(self, path) -> None:
        self.__path = path

    def escribir(self, texto):
        f = open(self.__path, 'wt')
        f.write(texto)
        f.close()

    def leer(selft):
        f = open(selft.__path, 'rt')
        texto = f.read()
        f.close()
        return texto