#Esta función captura cada excepción posible que el programador piense que puedan ocurrir

def divide():

    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))

        print("La dividión es :" + str(op1/op2))
    
    except ValueError:
        print("El valor introducido debe ser numérico")

    except ZeroDivisionError:
        print("No se puede dividir por 0")

    print("Cálculo finalizado")

divide()


#_______________________________________________________________

#Esta función captura todas las excepciones posibles, pero no define cuales pueden ser
#No se recomienda este tipo de captura

def divide2():

    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))

        print("La dividión es :" + str(op1/op2))
    
    except:
        print("Ha ocurrido un error")

    print("Cálculo finalizado")

divide2()

#_______________________________________________________________

#Con la instrucción finally, nos aseguramos que sí o sí, se ejecute el programa a partir
#de finally, aunque la función de error. Esto es útil por ejemplo para asegurarnos de 
#cerrar la base de datos en una aplicación, una vez terminada.

def divide3():

    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))

        print("La dividión es :" + str(op1/op2))
    
    except ValueError:
        print("El valor introducido debe ser numérico")

    except ZeroDivisionError:
        print("No se puede dividir por 0")

    finally:
        print("Cálculo finalizado")

divide3()