
# Polimorfismo (Descripcion)

Este proyecto implementa una jerarquía de clases en Python que utiliza el polimorfismo. La clase base Empleado define un método trabajar(), que es sobrescrito por las clases derivadas: Desarrollador, Diseñador y Gerente. Cada una proporciona su propia implementación del método.
## Clases

* Clase Empleado:
  * Descripción: Clase base que define el método trabajar().
  * Métodos:
  * trabajar():
  * Descripción: Método que debe ser sobrescrito por las subclases.
  * Retorno: Cadena vacía.

* Clase Desarrollador:
  * Descripción: Hereda de Empleado y redefine el método trabajar().
  * Métodos:
  * trabajar():
  * Descripción: Representa la actividad de un desarrollador.
  * Retorno: "Escribiendo código."

* Clase Diseñador:
  * Descripción: Hereda de Empleado y redefine el método trabajar().
  * Métodos:
  * trabajar():
  * Descripción: Representa la actividad de un diseñador.
  * Retorno: "Creando diseño gráfico."

* Clase Gerente:
  * Descripción: Hereda de Empleado y redefine el método trabajar().
  * Métodos:
  * trabajar():
  * Descripción: Representa la actividad de un gerente.
  * Retorno: "Gestionando el equipo."

## Ejemplo de uso

```python

from Diseñador import diseñador
from Desarrollador import desarrollador
from Gerente import gerente

def mostrar_trabajo(empleados):
    for empleado in empleados:
        print(empleado.trabajar())
        
empleados = [diseñador(),desarrollador(),gerente()]
mostrar_trabajo(empleados)
```