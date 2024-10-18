# Herencia multiple (Descripcion)

Este proyecto implementa herencia múltiple en Python mediante las clases Volador, Navegable y Hidroavion. La clase Hidroavion hereda de Volador y Navegable, lo que le permite navegar en el agua y volar en el aire.## Clases

* Clase Volador:

   * Descripción: Simula el comportamiento de vuelo.
   * Métodos:
   * volar():
   * Descripción: Indica que el objeto está volando.
   * Retorno: "Volando en el aire."

* Clase Navegable:

   * Descripción: Simula el comportamiento de navegación.
   * Métodos:
   * navegar():
   * Descripción: Indica que el objeto está navegando.
   * Retorno: "Navegando en el agua."

* Clase Hidroavion:

   * Descripción: Simula el comportamiento de un hidroavión.
   * Métodos:
   * navegar():
   * Descripción: Indica que el hidroavión está navegando.
   * Retorno: "El hidroavión está navegando."
   * volar():

 * Descripción: Indica que el hidroavión está volando.
 * Retorno: "El hidroavión está volando."



## Ejemplo de uso

```python
from Hidroavion import Hidroavion

if __name__ == "__main__":

    mi_hidroavion = Hidroavion()

    print(mi_hidroavion.navegar())  
    print(mi_hidroavion.volar())       
```