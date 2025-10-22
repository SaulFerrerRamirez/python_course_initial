class Cliente:
    def __init__(self, nombre: str, correo:str):
        self.nombre = nombre
        self.correo  = correo

    def validar_email(self) -> bool:
        """Valida estructura de mi correro"""
        return "@" in self.correo and "." in self.correo
    

client = Cliente("Saul", "c@rre.o")
print(client.validar_email())


        