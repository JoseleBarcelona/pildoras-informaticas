class Coche2:

    # __init__ es la manera de definir cual es el constructor (Es el método especial que tiene python
    # para que las propiedades del objeto instanciado en una clase, tenga un estado inicial)

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    # con dos guiones bajos, encapsulamos las propiedades para que no puedan ser modificados desde
    # fuera de la clase  (__largoChasis)

    def arranque(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            chequeo = self.__chequeo_interno()

        if self.__enMarcha and chequeo == True:
            return "\nEl coche está arrancado"

        elif self.__enMarcha and chequeo == False:
            return "algo ha ido mal en el arranque y ha sido imposible arrancar"

        else:
            return "El coche está apagado"

    def estado(self):
        print("El coche tiene", self.__ruedas, "ruedas, un ancho de", self.__anchoChasis, "y un largo de",
            self.__largoChasis)

    def __chequeo_interno(self):  #Encapsulamos el método, para que no pueda ser modificado fuera de la clase
        print("\nRealizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False


miCoche = Coche2()  # creamos un objeto, instancia, ejemplar que es lo mismo de la clase llamada
print(miCoche.arranque(True))
miCoche.estado()

print("\n-------------A continuación creamos el segundo objeto-------------\n")

miCoche2 = Coche2()
print(miCoche2.arranque(False))
# miCoche2.__ruedas=2  #No podemos variar el estado inicial, al haber encapsulado la propiedad ruedas
miCoche2.estado()

