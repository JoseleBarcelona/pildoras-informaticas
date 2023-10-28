import re

lista_nombres=['Ana',
                'Pedro',
                'María',
                'Rosa',
                'Sandra',
                'Celia']
for i in lista_nombres:
    if re.findall('[o-t]', i):
        print(i)
print('')

for i in lista_nombres:
    if re.findall('^[O-T]', i):
        print(i)

print('')

for i in lista_nombres:
    if re.findall('^[^O-T]', i): #Rango negado ^
        print(i)

lista_codigos=['Ma1',
                'Ma2',
                'Ma3',
                'Ma4',
                'Ma5',
                'Ma6',
                'Ma7',
                'Ma8',
                'MaA',
                'MaB',
                'MaC']
for i in lista_codigos:
    if re.findall('Ma[0-3A-B]', i):
        print(i)

# Pedro
# María
# Rosa
# Sandra
#
# Pedro
# Rosa
# Sandra
#
# Ana
# María
# Celia
# Ma1
# Ma2
# Ma3
# MaA
# MaB