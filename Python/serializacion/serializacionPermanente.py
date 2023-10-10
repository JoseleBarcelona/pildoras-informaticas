import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de ", self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)
    
class ListaPersonas:
    personas=[]

    def __init__(self):
        listaDePersonas=open("FicheroExterno", "ab+")
        listaDePersonas.seek(0)
        try:
            self.personas=pickle.load(listaDePersonas)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))

        except:
            print("El fichero está vacio")

        finally:
            listaDePersonas.close()
            del(listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPeersonasEnFicheroExterno()

    def mostrarPersonas(self):
        for i in self.personas:
            print(i)

    def guardarPeersonasEnFicheroExterno(self):
        listaDePersonas=open("ficheroExterno", "wb")
        pickle.dump(self.personas, listaDePersonas)
        listaDePersonas.close()
        del(listaDePersonas)

    def mostraInfoFicheroExterno(self):
        print("La información del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas()
persona=Persona("mama", "Femenino", 76)
miLista.agregarPersonas(persona)
miLista.mostraInfoFicheroExterno()


# Se cargaron 5 personas del fichero externo
# Se ha creado una persona nueva con el nombre de  mama
# La información del fichero externo es la siguiente:
# Sandra Femenino 29
# Núria Femenino 51
# Neus Femenino 24
# José Masculino 52
# papa Masculino 81
# mama Femenino 76