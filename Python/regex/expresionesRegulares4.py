import re

lista_nombres=['hombres',
               'mujeres',
               'mascotas',
               'niños',
               'niñas',
               'camión',
               'camion']

for i in lista_nombres:
    if re.findall('ñ', i):
        print(i)

print('')

for i in lista_nombres:
    if re.findall('niñ[oa]s', i):
        print(i)

print('')

for i in lista_nombres:
    if re.findall('cami[oó]n', i):
        print(i)
# niños
# niñas
#
# niños
# niñas
#
# camión
# camion
