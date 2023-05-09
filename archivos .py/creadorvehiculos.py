class vehiculo:
    def __init__(self, tipo, marca, modelo, cantidadpuertas, equipamiento):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.cantidadpuertas = cantidadpuertas
        self.equipamiento = equipamiento

    def __str__(self):
        return "El {} es un/a {} {}, cuenta con {} puertas y equipamiento {}"\
            .format(self.tipo, self.marca, self.modelo, self.cantidadpuertas, self.equipamiento)