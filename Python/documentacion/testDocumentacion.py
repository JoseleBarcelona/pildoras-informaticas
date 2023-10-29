#-----------------Primer test---------------------#

def areaTriangulo(base,altura):
    """
    Esta función calcula el área de un triángulo
    >>> areaTriangulo(3,6)
    9.0
    """

    return (base*altura)/2

#-----------------Segundo test---------------------#


def areaTriangulo2(base,altura):
    """
    Esta función calcula el área de un triángulo
    >>> areaTriangulo2(3,6)
    'El área del triángulo es: 9.0'
    """

    return "El área del triángulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()
