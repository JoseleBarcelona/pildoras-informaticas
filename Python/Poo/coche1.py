class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arranque(self):
        self.enmarcha=True

    def estado(self):
        if self.enmarcha:
            return "El coche está arrancado"
        else:
            return "El coche está apagado"

miCoche=Coche()

print("El largo del coche es de", miCoche.largoChasis,"cm")
print("El coche tiene", miCoche.ruedas, "ruedas")
miCoche.arranque()

print(miCoche.estado())
print("-------------A continuación creamos el segundo objeto-------------")

miCoche2=Coche()
print("El largo del coche es de", miCoche.largoChasis,"cm")
print("El coche tiene", miCoche.ruedas, "ruedas")
print(miCoche2.estado())

# El largo del coche es de 250 cm
# El coche tiene 4 ruedas
# El coche está arrancado
# -------------A continuación creamos el segundo objeto-------------
# El largo del coche es de 250 cm
# El coche tiene 4 ruedas
# El coche está apagado