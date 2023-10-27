import re

lista_URL=['http://pildorasinformatica.es',
           'http://pildorasinformatica.com',
           'ftp://pildorasinformatica.es',
           'ftp://pildorasinformatica.com']

for elemento in lista_URL:
    if re.findall('^ftp', elemento):
        print(elemento)

print('')

for elemento in lista_URL:
    if re.findall('.es$', elemento):
        print(elemento)

# ftp://pildorasinformatica.es
# ftp://pildorasinformatica.com
#
# http://pildorasinformatica.es
# ftp://pildorasinformatica.es