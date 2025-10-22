# args

# Argumentos posicionales
def procesar_datos(*args) -> None:
    """
        Recibe argumentos posicionales
    """
    print(f"Argumentos: {args}")


# Keyword arguments

def procesar_datos_kw(**kwargs) -> None:
    """
        Recibe argumentos posicionales
    """
    print(f"Argumentos: {kwargs}")

procesar_datos(10, 50, 5, 4, 2)
procesar_datos_kw(nombre = "Saul", status = True) # Regresa un tipo JSON