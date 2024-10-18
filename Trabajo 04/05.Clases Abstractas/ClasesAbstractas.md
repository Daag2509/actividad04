# Clases abstractas (Descripcion)

Este proyecto utiliza clases abstractas en Python para crear una jerarquía que modela empleados a tiempo completo y medio tiempo. La clase abstracta Empleado define los métodos abstractos calcular_salario() y mostrar_info(), que son implementados por las subclases EmpleadoTiempoCompleto y EmpleadoMedioTiempo.## Clases

* Clase Empleado (Abstracta):
  * Descripción: Clase base de la jerarquía que establece los métodos que deben ser implementados por las subclases.
  * Métodos:
  * calcular_salario():
   * Descripción: Método abstracto para calcular el salario del empleado.
   * Retorno: Salario del empleado.
  * mostrar_info():
   * Descripción: Método abstracto para mostrar la información del empleado.
   * Retorno: Información del empleado.

* Clase EmpleadoMedioTiempo:
  * Descripción: Hereda de Empleado e implementa los métodos para un empleado a medio tiempo.
  * Atributos:
  * nombre: Nombre del empleado.
  * horas_trabajadas: Total de horas trabajadas.
  * pago_por_hora: Pago recibido por hora trabajada.
  * Métodos:
  * calcular_salario():
   * Descripción: Calcula el salario basado en horas trabajadas y pago por hora.
   * Retorno: Salario calculado como horas_trabajadas * pago_por_hora.
  * mostrar_info():
   * Descripción: Muestra la información del empleado a medio tiempo.
   * Retorno: Detalles del empleado en formato de cadena.

* Clase EmpleadoTiempoCompleto:
  * Descripción: Hereda de Empleado e implementa los métodos para un empleado a tiempo completo.
  * Atributos:
  * nombre: Nombre del empleado.
  * salario_mensual: Salario mensual del empleado.
  * Métodos:
  * calcular_salario():
   * Descripción: Devuelve el salario mensual del empleado.
   * Retorno: Salario mensual en formato de cadena.
  * mostrar_info():
   * Descripción: Muestra la información del empleado a tiempo completo.
   * Retorno: Detalles del empleado en formato de cadena.
## Ejemplo de uso

```python
from EmpleadoDeMedioTiempo import EmpleadoMedioTiempo
from EmpleadoDeTiempoCompleto import EmpleadoTiempoCompleto

empleadoTiempoCompleto = EmpleadoTiempoCompleto("Gabriel Mendoza",120)
empleadoMedioTiempo = EmpleadoMedioTiempo("Jesus Mendoza",34,5)

#ejemplo con empleado de medio tiempo
print(empleadoMedioTiempo.mostrar_info())
print(empleadoMedioTiempo.calcular_salario())

print(empleadoTiempoCompleto.mostrar_info())
print(empleadoTiempoCompleto.calcular_salario())     
```