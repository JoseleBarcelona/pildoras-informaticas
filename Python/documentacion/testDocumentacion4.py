import math

def raizCuadrada(listaNumeros):
    """
    La función devuelve una lista con la raiz cuadrada de los elementos
    numéricos pasados por parámetros en otra lista.

    >>> lista=[]
    >>> for i in [4, 9, 16]: # Los >>> dice a python que debe hacer un test con los parámetros pasados
    ...     lista.append(i) #Los ... dice a python que lista.append() está anidada en el bucle for
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    >>> lista=[]
    >>> for i in [8, 4, -84, 7, 26, 6]:
    ...     lista.append(i)
    >>> raizCuadrada(lista)
    Traceback (most recent call last): #Ver video 77 de Píldoras Informáticas Python
        ...
    ValueError: math domain error


    """
    return [math.sqrt(n) for n in listaNumeros]

# print(raizCuadrada([9,16,25,36]))


import doctest
doctest.testmod()
