import re

nombre1="Sandra López"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="sandra Barbero"
nombre5="Sara Barbero"
nombre6="Lara Barbero"

if re.match("Sandra", nombre1):
#match() te busca si hay coincidencia en un patrón de búsqueda al comienzo de una cadena de texto
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

if re.match("López", nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

if re.match("Sandra", nombre4, re.IGNORECASE): #Admite tres parámetros
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

if re.match(".ara", nombre6):
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")


cadena1="Jara López"
cadena2="5484884848484"
cadena3="a9484884848484"

if re.match("\d", cadena2):
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado el número")

if re.search("López", nombre1):
#search() te busca si hay coincidencia en un patrón de búsqueda en toda una cadena de texto, no soólo al principio
    print("Hemos encontrado el nombre")
else:
    print("No hemos encontrado el nombre")

codigo1="ksdjkfssdfjklsdfhj71sdfkjbjdsfhjfd"
codigo2="jkadsfkhsdkjkssdkfasfsaggffgfsdfgf71sajkskjdsjjdksa"
codigo3="sdflkfjasljkdjfklfjkafjkadjk"

if re.search("71", codigo2):
#match() te busca si hay coincidencia en un patrón de búsqueda al comienzo de una cadena de texto
    print("Hemos encontrado el número")
else:
    print("No hemos encontrado el número")

# Hemos encontrado el nombre
# No hemos encontrado el nombre
# Hemos encontrado el nombre
# Hemos encontrado el nombre
# Hemos encontrado el número
# Hemos encontrado el nombre
# Hemos encontrado el número
