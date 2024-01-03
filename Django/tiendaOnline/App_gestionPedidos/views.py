from django.shortcuts import render
from django.http import HttpResponse
from App_gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from App_gestionPedidos.forms import Formulario_Contacto

# Create your views here.

def busqueda_productos(request): # Te lleva al archivo busqueda_productos

    return render(request, 'busqueda_productos.html')

def buscar(request): # Te devuelve lo return ponga, al pulsar el botón de buscar

    if request.GET['prd']:
        
        mensaje='Artículo buscado: %r' % request.GET['prd']
    else:
        mensaje='No has introducido nada'

    return HttpResponse(mensaje)

#--------------------------------------------------------------------------------------------------

def busqueda_productos_db(request): # Busca artículos en la base de datos

    return render(request, 'busqueda_productos_db.html')

def buscar_db(request): 

    if request.GET['prd']:
        
        producto=request.GET['prd'] #Almacenamos en la variable lo que rescatamos del la casilla del formulario
        if len(producto) >=20:
            mensaje='La longitud de la palabra insertada es demasiado larga'

        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto) #icontains es como el LIKE en SQL
            return render(request, 'resultados_busqueda.html', {'articulos':articulos, 'query':producto})
            
    else:
        mensaje='No has introducido nada'

    return HttpResponse(mensaje)

#--------------------------------------------------------------------------------------------------

def contacto(request):
    
    if request.method == 'POST':

        subject = request.POST['asunto']
        message = request.POST['mensaje'] + '     ' + request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['correo_recipiente@gmail.com']
        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'gracias.html')


    return render(request, 'contacto.html')

#--------------------------------------------------------------------------------------------------

def apiForms(request):

    if request.method == 'POST':

        miFormulario = Formulario_Contacto(request.POST)

        if miFormulario.is_valid():

            informacionFormulario = miFormulario.cleaned_data

            send_mail(informacionFormulario['asunto'], informacionFormulario['mensaje'], informacionFormulario.get('email', 'correo_saliente@gmail.com'), ['correo_recipiente@gmail.com'],)

            return render(request, 'gracias.html')
        
    else:

        miFormulario = Formulario_Contacto()

    return render(request, 'formulario_contacto.html', {'form':miFormulario})

