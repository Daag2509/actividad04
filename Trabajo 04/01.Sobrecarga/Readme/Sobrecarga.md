
# Sobrecarga (Descripcion)

Este proyecto implementa dos clases en Python: Vector y Transformador. La clase Vector se utiliza para calcular la norma de vectores en 2D y 3D, mientras que la clase Transformador permite transformar listas de números mediante la suma de sus elementos o multiplicándolos por un factor.
## Clases

## Clase vector

* calcular_norma(x, y):
  * Descripción: Calcula la norma de un vector en 2   dimensiones.
  * Parámetros:
  * x: Componente x del vector.
  * y: Componente y del vector.
  * Retorno: Norma del vector en 2D.

* calcular_norma(x, y, z):
  * Descripción: Calcula la norma de un vector en 3 dimensiones.
  * Parámetros:
  * x: Componente x del vector.
  * y: Componente y del vector.
  * z: Componente z del vector.
  * Retorno: Norma del vector en 3D.
## Ejemplo de uso

```python
from Vector import vector

if __name__ == "__main__":
    vector_2d = vector()
print("Norma del vector (3, 4):", vector_2d.calcular_norma(3, 4))   
print("Norma del vector (1, 2, 2):", vector_2d.calcular_norma(1, 2, 2))
```

## Clase Vector

La clase Transformador permite realizar operaciones sobre listas de números, ya sea sumando sus elementos o multiplicándolos por un factor.
## Clase transformador

* transformar(datos):
  * Descripción: Suma todos los elementos de una lista.
  * Parámetros:
  * datos: Lista de números a sumar.
  * Retorno: La suma total de los elementos.
* transformar(datos, factor):
  * Descripción: Multiplica cada elemento de la lista por un factor dado.
  * Parámetros:
  * datos: Lista de números.
  * factor: Valor por el cual se multiplican los elementos.
  * Retorno: Una nueva lista con los elementos multiplicados por el factor.
## Ejemplo de uso

```python
from Transformador import Transformador

lista_a_sumar = [1, 2, 3, 4, 5]
transformador_suma = Transformador(lista_a_sumar)
resultado_suma = transformador_suma.transformar()
print(f"Suma de elementos: {resultado_suma}")  
lista_a_multiplicar = [1, 2, 3]
factor = 3
transformador_multiplicacion = Transformador(lista_a_multiplicar, factor)
resultado_multiplicacion = transformador_multiplicacion.transformar()
print(f"Elementos multiplicados por {factor}: {resultado_multiplicacion}") 
```