from django.http import HttpResponse
import datetime
from django.template import Template, Context

#Primera vista
def saludo(request): 
    return HttpResponse('Hola amigos, esta es mi primera página con Django')

#Segunda vista
def despedida(request): 
    return HttpResponse('Hasta luego, gracias por usar Django con Python')

#Tercera vista
def saludoHtml(request):
    documento='''<html>
                <body>
                    <h1>Esto es una vista con html</h1>
                </body>
            </html>'''
    return HttpResponse(documento)

#Cuarta vista
def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento='''<html>
                <body>
                    <h1>Fecha y hora actual %s </h1>
                </body>
            </html>''' %fecha_actual
    return HttpResponse(documento)

#Primera vista con parámetros
def calculaEdad(request, agno):
    edadActual=52
    periodo=agno-2023
    edadFutura= edadActual+periodo
    documento='''<html>
                <body>
                    <p>En el año %s tendrás %s años</p>
                </body>
            </html>''' %(agno, edadFutura)
    return HttpResponse(documento)

#Segunda vista con parámetros
def calculaEdad2(request, edad, agno):
    periodo=agno-2023
    edadFutura= edad+periodo
    documento='''<html>
                <body>
                    <p>En el año %s tendrás %s años</p>
                </body>
            </html>''' %(agno, edadFutura)
    return HttpResponse(documento)

#Primera vista con plantillas
def saludoPlantilla(request):
    doc_externo=open("C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)
    return HttpResponse(documento)

#Segunda vista con plantillas y variables
def saludo_plantilla_variables(request):
    nombre='Josele'
    apellido='Barcelona'
    fecha=datetime.datetime.now()
    doc_externo=open("C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':nombre, 'apellido_usuario':apellido, 'fecha_actual':fecha})
    documento=plt.render(ctx)
    return HttpResponse(documento)

#Tercera vista con plantillas, variables y clases
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo_clases(request):
    p1=Persona('Josele', 'Barcelona')
    fecha=datetime.datetime.now()
    doc_externo=open("C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html")
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':p1.nombre, 'apellido_usuario':p1.apellido, 'fecha_actual':fecha})
    documento=plt.render(ctx)
    return HttpResponse(documento)