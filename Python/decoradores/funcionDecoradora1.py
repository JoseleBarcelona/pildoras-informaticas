def funcion_decoradora(funcion_parametro):
    def funcion_interna():

        #Accionesadicionales que decoran

        print("Vamos a realizar un cálculo:")

        funcion_parametro()

        #Accionesadicionales que decoran

        print("Cálculo realizado")
    return funcion_interna


@funcion_decoradora
def suma():
    print(8+2)
@funcion_decoradora
def resta():
    print(30-10)

suma()
resta()