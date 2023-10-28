def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args):
        #*args le dice a una función puede recibir un número indeterminado de parámetros

        #Accionesadicionales que decoran

        print("Vamos a realizar un cálculo:")

        funcion_parametro(*args)

        #Accionesadicionales que decoran

        print("Cálculo realizado")
    return funcion_interna


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)
@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

suma(7,5,5)
resta(12,10)
