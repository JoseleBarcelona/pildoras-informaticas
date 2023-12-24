from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from django.shortcuts import render

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
                    <h2>Fecha y hora actual %s </h2>
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
    doc_externo=open('C:/Programación/PildorasInformaticas/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla1.html')
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
    doc_externo=open('C:/Programación/PildorasInformaticas/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla2.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':nombre, 'ubicacion_usuario':ubicacion, 'fecha_actual':fecha})
    documento=plt.render(ctx)

    return HttpResponse(documento)

#Tercera plantilla con clases
class Persona(object):
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

def saludo_clases(request):
    p1=Persona('Núria', 'Barcelona')
    fecha=datetime.datetime.now()
    doc_externo=open('C:/Programación/PildorasInformaticas/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla2.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'nombre_usuario':p1.nombre, 'ubicacion_usuario':p1.ubicacion, 'fecha_actual':fecha})
    documento=plt.render(ctx)

    return HttpResponse(documento)

#Cuarta plantilla con listas y bucles
def saludo_bucles(request):
    temas=['Plantillas', 'Modelos', 'Formularios', 'Vistas', 'Despliegue']
    doc_externo=open('C:/Programación/PildorasInformaticas/PildorasInformaticasDjango/djangoProyecto1/djangoProyecto1/plantillas/plantilla3.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context({'temas_curso':temas})
    documento=plt.render(ctx)

    return HttpResponse(documento)

#Quinta plantilla con cargadores (Loader)
def saludo_cargadores(request):
    p1=Persona('Núria', 'Barcelona')
    fecha=datetime.datetime.now()
    doc_externo=loader.get_template('plantilla2.html')
    ctx={'nombre_usuario':p1.nombre, 'ubicacion_usuario':p1.ubicacion, 'fecha_actual':fecha}
    documento=doc_externo.render(ctx)

    return HttpResponse(documento)

#Sexta plantilla con el método render de la clase Django.shortcuts
def saludo_shortcut_render(request):
    p1=Persona('Núria', 'Barcelona')
    fecha=datetime.datetime.now()
    ctx={'nombre_usuario':p1.nombre, 'ubicacion_usuario':p1.ubicacion, 'fecha_actual':fecha}

    return render(request, 'plantilla2.html', ctx)

#Primera plantilla con herencia
def herencia(request):
    fecha=datetime.datetime.now()
    ctx={'dame_fecha':fecha}
    return render(request, 'herencia/plantilla_hija1.html', ctx)

#Segunda plantilla con herencia
def herencia2(request):
    fecha=datetime.datetime.now()
    ctx={'dame_fecha':fecha}
    return render(request, 'herencia/plantilla_hija2.html', ctx)
