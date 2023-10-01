def evaluaEdad(edad):

    if edad<0:
        raise TypeError("No has nacido todavía") 
    
    #Con raise lanzamos nosotros mismos una excepción que no esté definida en la librería de Python
    # ya que no pueden estar contemplados todos los casos que requieran cad código

    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate mucho"
    
print(evaluaEdad(-15))


# Traceback (most recent call last):
#   File "c:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasPython\Excepciones\prueba_excepciones3.py", line 18, in <module>
#     print(evaluaEdad(-15))
#           ^^^^^^^^^^^^^^^
#   File "c:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasPython\Excepciones\prueba_excepciones3.py", line 4, in evaluaEdad
#     raise TypeError("No has nacido todavía") 
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: No has nacido todavía