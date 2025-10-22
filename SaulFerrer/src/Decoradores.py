import time


def decorador(func):
    def envoltura():
        print("Inicio")
        func()
        print("Final")
    return envoltura


#funciopm_decorada = decorador(saludo)
#funciopm_decorada()


 # Genera un decorador que calcule el tiempo de ejecución de la funcion

def decorador_tiempo(func):
    def wrapper():
        inicio = time.time()
        func()
        final = time.time()
        print (f"Tiempo de ejecución: {inicio - final} segundos") 
    return wrapper


@decorador  #envuelve la funcion de "saludo" con el decorador de arriba
@decorador_tiempo 
def saludo():
    print("Hola mundo")

saludo()