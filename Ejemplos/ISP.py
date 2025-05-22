# Ejemplo de ISP (Interface Segregation Principle)

""""
    El principio de segregación de interfaces (ISP) establece que los clientes no
    deben verse obligados a depender de interfaces que no utilizan. En otras palabras,
    una clase no debe ser forzada a implementar métodos que no necesita. Esto
    promueve la creación de interfaces más específicas y enfocadas, en lugar de
    interfaces grandes y generales que pueden contener métodos innecesarios para
    algunas clases.

    Este diseño es incorrecto porque la clase Animal obliga a todas las subclases a
    implementar métodos que no son relevantes para todos los tipos de animales. Por ejemplo,
    un pez no necesita implementar el método volar().
"""


# Parte 1: Diseño inicial con incumplimiento de ISP

class Animal:
    def caminar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def nadar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def volar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")




"""
    Ahora, cada clase implementa solo los métodos que realmente necesita.
    Esto respeta el principio de segregación de interfaces (ISP) y hace que el diseño 
    sea más limpio y mantenible, ya que cada clase tiene una interfaz específica
    que refleja su comportamiento real, ya que por ejemplo, un pez no
    necesita implementar el método volar() y un pájaro no necesita implementar
    el método nadar().
"""

# Parte 2: Diseño corregido que respeta ISP
class volador:
    def volar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class nadador:
    def nadar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class caminador:
    def caminar(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Pajaro(caminador, volador):
    def caminar(self):
        print("El pájaro camina")
    
    def volar(self):
        print("El pájaro vuela")


class Pez(nadador):
    def nadar(self):
        print("El pez nada")


