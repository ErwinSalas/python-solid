"""
    El Primcipio de sustitución de Liskov (LSP) establece que los objetos de una clase
    base deben poder ser reemplazados por objetos de una clase derivada sin alterar
    el correcto funcionamiento del programa. En otras palabras, si una clase A es
    una subclase de B, entonces deberíamos poder usar objetos de A en lugar de
    objetos de B sin problemas.

    En este ejemplo, la clase PagoManual hereda de RealizarPago, pero no cumple
    con el principio de sustitución de Liskov (LSP) porque no puede procesar
    pagos automáticamente. Esto significa que no se puede sustituir un objeto
    de PagoManual en un contexto donde se espera un objeto de RealizarPago.
"""

#Clase de pago
class RealizarPago:
    def pagar(self, monto):
        raise NotImplementedError("Debe implementar el método pagar()")


#Esta clase hereda de manera correcta de RealizarPago
class RealizarPagoTarjeta(RealizarPago):
    def pagar(self, monto):
        print(f"[TARJETA] Pagando ₡{monto:.2f} con tarjeta de crédito")

#Esta clase hereda de manera correcta de RealizarPago
class RealizarPagoPaypal(RealizarPago):
    def pagar(self, monto):
        print(f"[PAYPAL] Pagando ₡{monto:.2f} con PayPal")

#Esta clase hereda de manera incorrecta de RealizarPago
# y rompe el principio de sustitución de Liskov (LSP)
class PagoManual(RealizarPago):
    def pagar(self, monto):
        raise Exception("[MANUAL] Este pago debe hacerse físicamente, no puede procesarse automáticamente")


# Esta función espera un objeto de tipo RealizarPago
def procesar_pago(pago: RealizarPago, monto):
    print("→ Procesando pago automático...")
    pago.pagar(monto)


print("=== ✅ Ejemplos que CUMPLEN LSP ===")
procesar_pago(RealizarPagoTarjeta(), 10000)
procesar_pago(RealizarPagoPaypal(), 5500)

print("\n=== ❌ Ejemplo que ROMPE LSP ===")
try:
    procesar_pago(PagoManual(), 8000)  
    # Esto lanza una excepcion porque PagoManual no puede procesar el pago automáticamente
except Exception as e:
    print(f"Error: {e}")




#Parte 2: Diseño corregido que respeta LSP
"""
    En este diseño, hemos separado los métodos de pago en dos jerarquías:
    1. PagoAutomatico: Métodos de pago que se pueden procesar automáticamente.
    2. PagoManual: Métodos de pago que requieren instrucciones manuales.
    Ambas jerarquías heredan de una clase base común llamada MetodoPago.
    Esto permite que los objetos de PagoAutomatico y PagoManual sean utilizados
    de manera intercambiable en el sistema, respetando el principio de sustitución
    de Liskov (LSP).
"""

print("\n=== ✅ DISEÑO REFACTORIZADO ===")

# Clase base para métodos de pago
# Esta clase define la interfaz común para todos los métodos de pago
class MetodoPago:
    def validar(self):
        print("Validando método de pago...")


#Esta clase hereda de manera correcta de MetodoPago
class PagoAutomatico(MetodoPago):
    def pagar(self, monto):
        raise NotImplementedError()

# Esta clase hereda de manera correcta de MetodoPago
class PagoManual(MetodoPago):
    def instrucciones(self):
        raise NotImplementedError()

# Esta clase hereda de manera correcta de PagoAutomatico
class PagoTarjeta(PagoAutomatico):
    def pagar(self, monto):
        print(f"[TARJETA] Pagando ₡{monto:.2f} con tarjeta")

# Esta clase hereda de manera correcta de PagoAutomatico
class PagoPaypal(PagoAutomatico):
    def pagar(self, monto):
        print(f"[PAYPAL] Pagando ₡{monto:.2f} con PayPal")

# Esta clase hereda de manera correcta de PagoManual ya que si implementara el pago automatico romperia LSP 
class PagoEfectivo(PagoManual):
    def instrucciones(self):
        print("[EFECTIVO] Por favor, presente el monto exacto en ventanilla para completar su pago.")

# Esta función espera un objeto de tipo PagoAutomatico
def procesar_pago_automatico(pago: PagoAutomatico, monto):
    print("→ Procesando pago automático (versión segura)...")
    pago.validar()
    pago.pagar(monto)

# Esta función espera un objeto de tipo PagoManual
def mostrar_instrucciones_pago_manual(pago: PagoManual):
    print("→ Instrucciones para pago manual:")
    pago.validar()
    pago.instrucciones()


""" 
    Uso correcto de ambas jerarquías, las de pago tarjeta y paypal utilizando 
    la interfaz de pago automatico y la de efectivo utilizando
    la interfaz de pago manual, para no romper LSP
"""
procesar_pago_automatico(PagoTarjeta(), 12000)
procesar_pago_automatico(PagoPaypal(), 7800)
mostrar_instrucciones_pago_manual(PagoEfectivo())
