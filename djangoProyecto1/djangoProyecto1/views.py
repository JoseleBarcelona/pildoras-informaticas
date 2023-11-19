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

#Primera plantilla
def saludo_plantilla(request):
    doc_externo=open('C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento=plt.render(ctx)

    return HttpResponse(documento)

#Segunda plantilla con variables
def saludo_variables(request):
    nombre='Josele'
    ubicacion='Barcelona'
    fecha=datetime.datetime.now()
    doc_externo=open('C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':nombre, 'ubicacion_usuario':ubicacion, 'fecha_actual':fecha})
    documento=plt.render(ctx)

    return HttpResponse(documento)

#tercera plantilla con clases
class Persona(object):
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

def saludo_clases(request):
    p1=Persona('Núria', 'Barcelona')
    fecha=datetime.datetime.now()
    doc_externo=open('C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':p1.nombre, 'ubicacion_usuario':p1.ubicacion, 'fecha_actual':fecha})
    documento=plt.render(ctx)

    return HttpResponse(documento)

#cuarta plantilla con listas y bucles
class Persona(object):
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

def saludo_bucles(request):
    p1=Persona('Núria', 'Barcelona')
    temas=['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    fecha=datetime.datetime.now()
    doc_externo=open('C:/Users/34660/.vscode/Visual Studio Code/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla2.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':p1.nombre, 'ubicacion_usuario':p1.ubicacion, 'fecha_actual':fecha, 'temas_curso':temas})
    documento=plt.render(ctx)

    return HttpResponse(documento)