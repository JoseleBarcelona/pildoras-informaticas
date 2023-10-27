import re

cadena="Vamos a aprender expresiones regulares para aprender Python. Python es un lenguaje para aprender programación"
print(re.search("aprender", cadena)) #Esto nos devuelve un objeto que coincide con el texto buscado

# ---------------Manera de ver la coincidencia en consola--------------

textoBuscar="aprender"

if re.search(textoBuscar, cadena) is not None: #Si no encuentra el texto, te devuelve un None
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

textoEncontrado=re.search(textoBuscar, cadena) #El objeto creado lo guardamos en una variable
print(textoEncontrado.start()) #Nos dice el número de caracter donde empieza el texto encontrado
print(textoEncontrado.end()) #Nos dice el caracter donde termina la palabra encontrada
print(textoEncontrado.span()) #Nos dice el caracter de comienzo y el caracter final

print(re.findall(textoBuscar, cadena)) #Encuentra todas las coincidencias del texto buscado
print(len(re.findall(textoBuscar, cadena)))
print(re.search(textoBuscar, cadena).start())

# <re.Match object; span=(8, 16), match='aprender'>
# He encontrado el texto
# 8
# 16
# (8, 16)
# ['aprender', 'aprender', 'aprender']
# 3
# 8
