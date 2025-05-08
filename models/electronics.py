
class ElectronicDevice:
    def __init__(self, modelo, marca, precio):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio
        self.reparado = False
        self.vendido = False


class Monitor(ElectronicDevice):
    def __init__(self, modelo, marca, precio, pulgadas):
        super().__init__(modelo, marca, precio)
        self.pulgadas = pulgadas
        
class Laptop(ElectronicDevice):
    def __init__(self, modelo, marca, precio, pulgadas,cpu,memoria,ram):
        super().__init__(modelo, marca, precio)
        self.cpu = cpu
        self.memoria = memoria
        self.ram = ram