from models.electronics import Monitor,Laptop

class CarritoDeCompras:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def mostrar(self):
        for item in self.items:
            print(f"{item.__class__.__name__}: {item.marca} {item.modelo} - ${item.precio}")

class Compra:
    def realizar_compra(self, carrito: CarritoDeCompras):
        raise NotImplementedError("Debe ser implementado en otras clases o da error jajaja")

class ComprarMonitor(Compra):
    def __init__(self, monitor:Monitor):
        super().__init__()
        self.monitor = monitor
    
    def realizar_compra(self, carrito: CarritoDeCompras):
        carrito.agregar(self.monitor)


class ComprarLaptop(Compra):
    def __init__(self, laptop:Laptop):
        super().__init__()
        self.laptop = laptop
    
    def realizar_compra(self, carrito: CarritoDeCompras):
        carrito.agregar(self.laptop)


