# Herencia simple (Descripcion)

Este proyecto implementa dos clases en Python utilizando herencia simple: Vehiculo y Carro. La clase Carro hereda de la clase base Vehiculo y proporciona implementaciones específicas para los métodos arrancar() y parar().## Clases

* Clase Vehiculo:
  * Descripción: Clase base que define los métodos arrancar() y parar(), los cuales pueden ser sobrescritos por las subclases.
  * Métodos: 

  * arrancar():
  * Descripción: Indica que el vehículo está en proceso de arranque.
  * Parámetros: Ninguno.
  * Retorno: Cadena de texto que indica que el vehículo está arrancando.

* parar():

  * Descripción: Indica que el vehículo ha detenido su funcionamiento.
  * Parámetros: Ninguno.
  * Retorno: Cadena de texto que indica que el vehículo se ha detenido.



## Ejemplo de uso

```python
from Carro import carro

if __name__ == "__main__":
    mi_carro = carro()

    print(mi_carro.arrancar()) 
    print(mi_carro.parar())      
```