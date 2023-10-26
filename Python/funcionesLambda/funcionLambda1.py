#---------------------función normal--------------------#

def area_triangulo(base, altura):
    return (base*altura)/2
print(area_triangulo(5,6))
print(area_triangulo(8,10))

#------------función Lambda (función anónima)------------#

areaTriangulo=lambda base, altura:(base*altura)/2
#Los : es como un return, le decimos lo que queremos que nos devuelva
print(areaTriangulo(5,6))
print(areaTriangulo(8,10))

al_cubo=lambda numero:numero**3 #número elevado al cubo
print(al_cubo(3))
al_cubo2=lambda numero:pow(numero,3) #función para exponentes
print(al_cubo(3))

destaca_valor=lambda  comision:"¡{}! €".format(comision)
comision_Ana=15585
print(destaca_valor(comision_Ana))