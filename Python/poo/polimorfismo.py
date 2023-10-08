class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo con dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 8 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Camion()
# miVehiculo=Coche()
# miVehiculo=Moto()
desplazamientoVehiculo(miVehiculo)