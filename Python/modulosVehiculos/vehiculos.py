
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
        
class Furgoneta(Vehiculos):
    
    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "la furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"
    
class Moto(Vehiculos): #Esta es la manera de heredar los atributos y métodos de una clase padre
    #pass #Pongo un pass para no construir la clase de momento y no me de error

    hacerCaballito=""
    def caballito(self):
        self.hacerCaballito="Voy haciendo el caballito con mi moto"

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.arranque, 
                "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hacerCaballito)
        
class VehiculosElectricos():

    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

class BicicletaElectrica(VehiculosElectricos, Vehiculos):
    pass


