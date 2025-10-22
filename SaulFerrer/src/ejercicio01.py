#Comentario en una línea

"""
    Para comentarios multilinea
    se utiliza triple comilla
"""

variable_numero = 3

print(type(variable_numero))  #Muestra el tipo de variable


variable_numero = "Layna"

print(type(variable_numero)) 

#//////////////////////////////////////////////////////////////////////////
a, b, c = 1, 2, 3

print(a + b)

a = b = c

print(a*a)

#//////////////////////////////////////////////////////////////////////////


"""
    Compresiones
    Lista de números
"""


numeros = [1,2,3,4,5]

pares = [numero for numero in numeros if numero % 2 == 0]

print(type(pares))
print(pares)