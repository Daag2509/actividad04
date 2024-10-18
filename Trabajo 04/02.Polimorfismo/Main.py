from Diseñador import diseñador
from Desarrollador import desarrollador
from Gerente import gerente

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())
        
empleados = [diseñador(),desarrollador(),gerente()]
mostrar_trabajo(empleados)