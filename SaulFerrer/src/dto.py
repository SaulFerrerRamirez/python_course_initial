from dataclasses import dataclass

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

#   Dataclass

@dataclass
class PersdonaDTO:
    nombre: str
    edad: int
    cat: str

person = PersdonaDTO("Saul", 22, "Trainee")

print(person)
