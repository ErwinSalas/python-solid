from services.MiniProyectoSolid import CarritoDeCompras,Laptop,Monitor,ComprarMonitor,ComprarLaptop

carrito = CarritoDeCompras()

laptop = Laptop("ThinkPad", "Lenovo", 850.0, 14, "i7", "512GB SSD", "16GB")
monitor = Monitor("AOC24", "AOC", 150.0, 24)

ComprarMonitor(monitor).realizar_compra(carrito)
ComprarLaptop(Laptop).realizar_compra(carrito)



carrito.mostrar()
