# El * delante de un argumento de una función, le dice al programa que va a recibir un número indeterminado de elementos en forma de tupla
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        yield elemento


ciudadesDevueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudadesDevueltas)) #devuelve el primer elemento
print(next(ciudadesDevueltas))
print("")


def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        for subelemento in elemento: #for anidado
            yield subelemento


ciudadesDevueltas = devuelveCiudades2("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudadesDevueltas)) #devuelve el primer subelemento
print(next(ciudadesDevueltas))
print("")

def devuelveCiudades3(*ciudades):
    for elemento in ciudades:
        yield from elemento #yield from simplifica el código de un for anidado


ciudadesDevueltas = devuelveCiudades3("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudadesDevueltas)) #devuelve el primer subelemento
print(next(ciudadesDevueltas))
