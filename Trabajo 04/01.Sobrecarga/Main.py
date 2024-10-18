from Vector import vector
from Transformador import Transformador


##Ejemplo del uso(Vector)
print("Ejemplo 01 Vector")
if __name__ == "__main__":
    vector_2d = vector()
print("Norma del vector (3, 4):", vector_2d.calcular_norma(3, 4))   
print("Norma del vector (1, 2, 2):", vector_2d.calcular_norma(1, 2, 2))   

##Ejemplo del uso(Transformador)
print("Ejemplo 02 Transformador")
lista_a_sumar = [1, 2, 3, 4, 5]
transformador_suma = Transformador(lista_a_sumar)
resultado_suma = transformador_suma.transformar()
print(f"Suma de elementos: {resultado_suma}")  
lista_a_multiplicar = [1, 2, 3]
factor = 3
transformador_multiplicacion = Transformador(lista_a_multiplicar, factor)
resultado_multiplicacion = transformador_multiplicacion.transformar()
print(f"Elementos multiplicados por {factor}: {resultado_multiplicacion}")  
