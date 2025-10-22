def saludar(nombre: str) -> str:
   
    '''Función que regresa un saludo'''
    
    return f"Hola {nombre}"  #Concatenar con variable


print(saludar("Saúl"))

#//////////////////////////////////////////////////////////////////////////

'''Función con argumento por default'''


def saludo_generico(nombre = "Usuario"):
    return f"Hola {nombre}"


print(saludo_generico("Saúl"))


#//////////////////////////////////////////////////////////////////////////

"""Funcion con argumento kwargs



   Lambda
"""

def suma(num1: int, num2: int) -> int:
    '''Suma de 2 numeros'''
    return num1+num2

suma_lambda = lambda n1,n2 : n1 + n2

print(suma(2,3))
print(suma_lambda(2,3))


#//////////////////////////////////////////////////////////////////////////

"""
    Map y Filter


    Map: Modifica cada elemento de una lista
"""
lista_numeros = [1,2,3,4,5]


set = {1,2,3,3}

print(set)

tipo_dato = type(map(lambda x: x**2, lista_numeros))

print(f"Tipo de dato {tipo_dato}")
cuadrados = list(map(lambda x: x**2, lista_numeros))


print(cuadrados)


"""
    Filter: Selecciona cada elemento de la lista
"""

pares = list(filter(lambda x: x%2 == 0, lista_numeros))

print(pares)