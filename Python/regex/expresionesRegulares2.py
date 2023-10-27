import re

lista_nombres=['Ana Gómez',
               'María Martín',
               'Sandra López',
               'Santiago Martín',
               'Sandra Martín',
               ]

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento): #Todo lo que empieze por Sandra
        print(elemento)

print("")

for elemento1 in lista_nombres:
    if re.findall('Martín$', elemento1): #Todo lo que termine por Martín
        print(elemento1)

# Sandra López
# Sandra Martín
#
# María Martín
# Santiago Martín
# Sandra Martín
