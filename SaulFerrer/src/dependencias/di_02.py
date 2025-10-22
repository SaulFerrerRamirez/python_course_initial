
from abc import ABC, abstractmethod
from dependency_injector import containers, providers

class IRepositorioBD(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass

class RepositorioBD(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Pedido {pedido} almacenado exitosamente")

class ApiTercerosAdapter(IRepositorioBD):
    def guardar(self, pedido):
        print(f"Guardado pero de forma distinta: {pedido}" )

class ServicioPedido:
    def __init__(self, repositorio: IRepositorioBD):
        self.repo = repositorio

    def crear_pedido(self, pedido:str):
        print("Notificacion por mensaje")
        print("Impresion de orden")
        self.repo.guardar(pedido)
        print("Noificacion de almacenado")


#Dependency injector with pip package
class Contenedor(containers.DeclarativeContainer):
    
    repositorio = providers.Singleton(RepositorioBD)
    service = providers.Factory(ServicioPedido, repositorio=repositorio)

container = Contenedor()
service_instance = container.service()
service_instance_two = container.service()

service_instance.crear_pedido("Pan de Muerto")

print(service_instance_two is service_instance)