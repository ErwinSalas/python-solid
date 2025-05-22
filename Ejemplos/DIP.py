"""
    El principio de  inversión de dependencias (DIP) establece que las clases de alto nivel
    no deben depender de clases de bajo nivel, sino de abstracciones. Esto significa que
    deberíamos utilizar interfaces o clases abstractas para definir el comportamiento
    esperado, y las clases concretas deben implementar esas interfaces. Esto ayuda a
    mantener el código flexible y fácil de modificar.
"""


# Parte 1: Diseño inicial con incumplimiento de DIP
"""
    En este diseno la clase Application depende directamente de la clase
    MySQLDatabase, lo que significa que si queremos cambiar la base de datos
    a otro sistema, tendríamos que modificar la clase Application.
"""
class MySQLDatabase:
    def connect(self):
        print("Conectando a la base de datos MySQL")
    
class Application:
    def __init__(self):
        self.db = MySQLDatabase()



# Parte 2: Diseño corregido que respeta DIP
"""
    En este diseño, hemos creado una interfaz Database que define el comportamiento
    esperado para las conexiones a la base de datos, y la clase Application
    depende de esta interfaz en lugar de depender directamente de una implementación
"""
class Database:
    def connect(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class MySQLDatabase(Database):
    def connect(self):
        print("Conectando a la base de datos MySQL")

class Application:
    def __init__(self, db: Database):
        self.db = db
