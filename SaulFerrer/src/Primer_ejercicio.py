"""
    Ejercicio precio de producto con IVA
"""

def precio_final (precio: int) -> float:
    precio_f = (precio * 0.16) + precio
    return precio_f


cantidad = int(input("Ingresa precio  "))

print (precio_final(cantidad))

