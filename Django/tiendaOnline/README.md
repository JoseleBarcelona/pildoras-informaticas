### Pasos a seguir para construir un aplicación con Django dentro de un proyecto:  
#### 1. Buscamos en el directorio donde tenemos la carpeta en la que vamos a crear el proyuecto 

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango`  
  
- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango>` *django-admin startproject tiendaOnline*

- `cd tiendaOnline`
  
- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py startapp App_gestionPedidos*
---
### models.py  
#### 2. Creamos los modelos que vayamos a usar en nuestra aplicación en el archivo models.py
```python	
    from django.db import models


    class Clientes(models.Model):
        nombre=models.CharField(max_length=30)
        direccion=models.CharField(max_length=50)
        email=models.EmailField()
        telefono=models.CharField(max_length=9)

    class Articulos(models.Model):
        nombre=models.CharField(max_length=30)
        seccion=models.CharField(max_length=20)
        precio=models.IntegerField()

    class Pedidos(models.Model):
        numero=models.IntegerField()
        fecha=models.DateField()
        entregado=models.BooleanField()
```
---

### settings.py  
#### 3. Le decimos a Django que hemos creado una nueva aplicación en el archivo settings.py
```python	
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App_gestionPedidos',
    ]
```
---
#### 4. Comprobamos que la app se haya instalado correctamente

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py check App_gestionPedidos*  

    ``Si todo es correcto, se mostrará este mensaje en el shell:``  
   
    ```
    System check identified no issues (0 silenced).
    ```
---
#### 5. Creamos nuestra base de datos

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py makemigrations*    
  
  `Si todo es correcto, se mostrará este mensaje en el shell:`

    ```
    Migrations for 'App_gestionPedidos': 
    App_gestionPedidos\migrations\0001_initial.py
        -Create model Articulos
        -Create model Clientes
        -Create model Pedidos

    ```
---
#### 6. Le decimos a Django, que debe insertar las tablas que hemos creado, en la base de datos recién creada, en dos pasos.

A) Le decimos a Django que primero genere el código SQL de los modelos creados  
- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py sqlmigrate App_gestionPedidos 0001*  
  
    `Si todo es correcto, se mostrará este mensaje en el shell:`
        ```
        BEGIN;
            Create model Articulos

        CREATE TABLE "App_gestionPedidos_articulos" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(30) NOT NULL, "seccion" varchar(20) NOT NULL, "precio" integer NOT NULL);

            Create model Clientes

        CREATE TABLE "App_gestionPedidos_clientes" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "nombre" varchar(30) NOT NULL, "direccion" varchar(50) NOT NULL, "email" varchar(254) NOT NULL, "telefono" varchar(9) NOT NULL);

            Create model Pedidos

        CREATE TABLE "App_gestionPedidos_pedidos" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "numero" integer NOT NULL, "fecha" date NOT NULL, "entregado" bool NOT NULL);

        COMMIT;
        ```
B) Migramos las tablas a la base de datos
- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py migrate*
---
### Resumen de los pasos a seguir con la shell

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango`

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango>` *django-admin startproject tiendaOnline*

- `cd tiendaOnline`

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py startapp App_gestionPedidos*

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py check App_gestionPedidos*

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py makemigrations*

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py sqlmigrate App_gestionPedidos 0001*

- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py migrate*

### Pasos para Insert, update, delete en la base de datos
- `C:\Users\34660\.vscode\Visual Studio Code\PildorasInformaticasDjango\tiendaOnline>` *python manage.py shell*  
  
- `In [1]: from App_gestionPedidos.models import Articulos`
  
- `In [2]: art=Articulos(nombre='mesa', seccion='decoració', precio=90)`
  
- `In [3]: art.save()`
  
- `In [4]: art2=Articulos(nombre='camisa', seccion='confección', precio=75)`
  
- `In [5]: art2.save()`

- `In [6]: art3=Articulos.objects.create(nombre='taladro', seccion='ferretería', precio=65)`
  
- `In [7]: art.seccion='decoración'`

- `In [9]: art4=Articulos.objects.get(id=1)`

- `In [10]: art4.delete()`

- `Out[10]: (1, {'App_gestionPedidos.Articulos': 1})`

- `In [11]: lista=Articulos.objects.all()`

- `In [12]: lista`

- `Out[12]: <QuerySet [<Articulos: Articulos object (2)>, <Articulos: Articulos object (3)>]>`

-  `In [15]: lista.query.__str__()`

- `Out[15]: 'SELECT "App_gestionPedidos_articulos"."id", "App_gestionPedidos_articulos"."nombre", "App_gestionPedidos_articulos"."seccion", "App_gestionPedidos_articulos"."precio" FROM "App_gestionPedidos_articulos"'`

