import pickle

class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.arranque=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.arranque=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.arranque, 
                "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
        
coche1=Vehiculos("Mazda", "6")
coche2=Vehiculos("Renault", "5")
coche3=Vehiculos("Seat", "125")

coches=[coche1, coche2, coche3]

fichero_escritura=open("losCoches", "wb" )
pickle.dump(coches, fichero_escritura)
fichero_escritura.close()
del fichero_escritura

fichero_lectura=open("losCoches", "rb")
carga_fichero=pickle.load(fichero_lectura)
fichero_lectura.close()
del (fichero_lectura)

for c in carga_fichero:
    print(c.estado())

# Marca:  Renault
# Modelo:  5
# En marcha:  False
# Acelerando:  False
# Frenando:  False
# None
# Marca:  Seat
# Modelo:  125
# En marcha:  False
# Acelerando:  False
# Frenando:  False
# None