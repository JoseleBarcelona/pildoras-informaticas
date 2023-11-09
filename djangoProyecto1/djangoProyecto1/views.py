from django.http import HttpResponse
import datetime

#Primera vista
def saludo(request): 
    return HttpResponse('Hola amigos, esta es mi primera página con Django')

#Segunda vista
def despedida(request): 
    return HttpResponse('Hasta luego, gracias por usar Django con Python')

#Tercera vista
def saludoHtml(request):
    texto='''<html>
                <body>
                    <h1>Esto es una vista con html</h1>
                </body>
            </html>'''
    return HttpResponse(texto)

#Cuarta vista
def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    texto='''<html>
                <body>
                    <h1>Fecha y hora actual %s </h1>
                </body>
            </html>''' %fecha_actual
    return HttpResponse(texto)

#Primera vista con parámetros
def calculaEdad(request, agno):
    edadActual=52
    periodo=agno-2023
    edadFutura= edadActual+periodo
    texto='''<html>
                <body>
                    <p>En el año %s tendrás %s años</p>
                </body>
            </html>''' %(agno, edadFutura)
    return HttpResponse(texto)

#Segunda vista con parámetros
def calculaEdad2(request, edad, agno):
    periodo=agno-2023
    edadFutura= edad+periodo
    texto='''<html>
                <body>
                    <p>En el año %s tendrás %s años</p>
                </body>
            </html>''' %(agno, edadFutura)
    return HttpResponse(texto)

