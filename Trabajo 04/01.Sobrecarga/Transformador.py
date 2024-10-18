class Transformador:
    def __init__(self, *args):
        self.datos = args

    def transformar(self):
        if len(self.datos) == 1:
            return sum(self.datos[0])
        
        elif len(self.datos) == 2:
            lista, factor = self.datos
            return [dato * factor for dato in lista]
        else:
            raise ValueError("El número de componentes debe ser 1 o 2.")