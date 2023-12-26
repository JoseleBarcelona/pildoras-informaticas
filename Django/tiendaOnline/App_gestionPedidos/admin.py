from django.contrib import admin
from App_gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display=('nombre', 'direccion', 'telefono') #muestra en el panel de admin los campos que queremos
    search_fields=('nombre', 'telefono') #barra de búsqueda

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=('seccion','nombre',) #Crea una interfaz que filtra por sección y por nombre(Ponemos una , al final ya que es una tupla)
    
class PedidosAdmin(admin.ModelAdmin):
    list_filter=('fecha',)
    list_display=('numero', 'fecha', 'entregado', 'id') 
    date_hierarchy='fecha' #crea en la parte superior de admin un historial de fechas

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
