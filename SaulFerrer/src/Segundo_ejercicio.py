
def conteo_fibonacci(limit: int):

    a, b = 0, 1
    
    for i in range(limit):
        yield a
        a , b = b, a + b
        
    
for numero in conteo_fibonacci(10):
    print(numero)


    