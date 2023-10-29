def areaTriangulo2(base,altura):
    """
    Esta función calcula el área de un triángulo

    >>> areaTriangulo2(3,6)
    'El área del triángulo es: 9.0'

    >>> areaTriangulo2(4,5)
    'El área del triángulo es: 10.0'

    >>> areaTriangulo2(9,3)
    'El área del triángulo es: 13.5'

    """

    return "El área del triángulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()
