class Producto:
    ''' Clase producto. Propiedades de un producto '''
    def __init__(self, nombre: str, precio: float):
        '''Constructor de clase'''
        self.nombre = nombre
        self.precio = precio

producto_uno = Producto("Pan Integral", 3.3)

print(f"Producto 1: {producto_uno.nombre} con costo de {producto_uno.precio}")

#Property y setter

class ProductoSetter:
    ''' Clase producto. Propiedades de un producto '''
    def __init__(self, nombre: str, precio: float):
        '''Constructor de clase'''
        self.nombre = nombre
        self.precio = precio

    @property #Protege el acceso ala propiedad
    def precio(self) -> float:
        '''Getter. Nos permite acceder a la propiedad de .precio pero sin pasarle los parentesis'''
        return self._precio
    
    @precio.setter
    def precio(self, value: float):
        '''Nos permite modificar el valor de la propiedad y aplicar validaciones'''
        if value <= 0:
            raise ValueError("El precio debe ser mayor a cero") #Manda un mensaje de error
        self._precio = value


    def __str__(self) -> str:
        '''Metodo especial que nos permite el llamado para convertirlo a cadena de texto'''
        return f"---El producto {self.nombre} tiene un costo de {self.precio}"

producto_dos = ProductoSetter("Pan Integral", 32.3)

print(producto_dos) #Imprime la funcion __str

print(f"Producto 1: {producto_dos.nombre} con costo de {producto_dos.precio}")
producto_dos.precio = 50
print(f"Producto 1: {producto_dos.nombre} con costo de {producto_dos.precio}")