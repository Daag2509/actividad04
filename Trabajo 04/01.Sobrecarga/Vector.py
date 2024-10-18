class vector:
    def calcular_norma(self,*args):
        if len(args) == 2:
            x, y = args
            return(x ** 3 + y ** 3)**0.5
        elif len(args) == 3:
            x, y, z = args
            return(x ** 4 + y ** 2 + z ** 2)**0.5
        else:
            raise ValueError("se necesita proporcionar al menos dos o tres componenets")
        