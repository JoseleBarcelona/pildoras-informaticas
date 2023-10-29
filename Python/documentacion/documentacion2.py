from modulosMatematicos import funcionesMatematicas

class Areas:
    """Esta clase calcula las áreas de diferentes figuras geométricas"""
    def areaCuadrado(lado):
        """Esta función calcula el área de un cuadrado
        elevando al cuadrado el lado pasado por parámetro"""

        return "El área del cuadrado es: " + str(lado*lado)

    def areaTriangulo(base, altura):
        """Esta función calcula el área de un triángulo
        utilizando los parámetros base y altura"""

        return "El área del triángulo es:" + str((base*altura)/2)

help(Areas)
help(funcionesMatematicas)