# yield 



def conteo_to_limit(limit: int):
    """Cuenta desde 0 al limite"""
    print("Inicio de función tradicional")
    list = []
    for i in range(limit):
        print("En la posicion", i) #Se recomienfa usar el  f"Mensaje {variable}"
        list.append(i)
        return list
    print("Finaliza la función tradicional")

def conteo_gen(limit: int):
    """Conteo de 0 al limite"""
    print("Inicio del generador")
    
    for i in range(limit):
        print("En la posicion " , i)
        yield i
    print("Fin del generador")

#conteo_to_limit(10)
print(type(conteo_gen(10)))
print(type(conteo_to_limit(10)))

#for numero in conteo_gen(5):
#    print("En generador ", numero)

#for numero in conteo_to_limit(5):
#    print("Conteo tradicional ", numero)