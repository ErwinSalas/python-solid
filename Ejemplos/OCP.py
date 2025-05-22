"""
    El principio de abierto/cerrado (OCP) establece que las clases deben estar abiertas para la
    extensión pero cerradas para la modificación. Esto significa que deberíamos poder
    agregar nuevas funcionalidades sin modificar el código existente.
"""

# Parte 1: Diseño inicial con incumplimiento de OCP

"""
    En este diseño, la función calcularDescuento() no es extensible. Si queremos
    agregar un nuevo tipo de descuento, tendríamos que modificar la función
    directamente. Esto va en contra del principio de abierto/cerrado (OCP).

"""
def calculateDiscount(type,amount):
    if type == "student":
        return amount * 0.8  
    elif type == "senior":
        return amount * 0.7  
    else:
        return amount
    

# Parte 2: Diseño corregido que respeta OCP
"""
    En este diseño, hemos creado una clase base Descuento y subclases para cada
    tipo de descuento. Esto permite agregar nuevos tipos de descuento sin
    modificar el código existente, cumpliendo así con el principio de abierto/cerrado (OCP).
"""

class Descuento:
    def aplicar(self, monto):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class DescuentoEstudiante(Descuento):
    def aplicar(self, monto):
        return monto * 0.8

class DescuentoSenior(Descuento):
    def aplicar(self, monto):
        return monto * 0.7

