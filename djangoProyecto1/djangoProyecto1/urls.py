"""
URL configuration for djangoProyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from djangoProyecto1.views import saludo, despedida, saludoHtml, dameFecha, calculaEdad, calculaEdad2, saludoPlantilla
from djangoProyecto1.views import saludo_plantilla_variables, saludo_clases

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('despedida/', despedida),
    path('saludoHtml/', saludoHtml),
    path('fecha/', dameFecha),
    path('edades/<int:agno>', calculaEdad),
    path('edades2/<int:edad>/<int:agno>', calculaEdad2),
    path('saludoPlantilla/', saludoPlantilla),
    path('saludo_variables/', saludo_plantilla_variables),
    path('saludo_clases/', saludo_clases),
]
