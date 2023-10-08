#Este es el archivo tipo para poder distribuir un paquete en la red a través del medio que prefieras
#y poder luego instalarlo localmente en tu ordenador directamente dentro de python y el interprete
#pueda llamarlo desde cualquier ruta que se quiera.

from setuptools import setup

setup(

    name="paquetecalculos",
    version="1.0",
    description="Paquete para hacer redondeos y potencia",
    author="Josele",
    author_email="josele@mcmobres.com",
    url="www.google.com",
    packages=["paqueteCalculos", "paqueteCalculos.calculosAvanzados"]

)