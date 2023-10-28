def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args, **kwargs):
        #*args le dice a una función puede recibir un número indeterminado de parámetros
        #**kwargs le dice a la funcion que va a recibir argumentos con clave, valor 
        #Accionesadicionales que decoran

        print("Vamos a realizar un cálculo:")

        funcion_parametro(*args, **kwargs)

        #Accionesadicionales que decoran

        print("Cálculo realizado")
    return funcion_interna


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))

suma(7,5,5)
resta(12,10)
potencia(base=5, exponente=3)
