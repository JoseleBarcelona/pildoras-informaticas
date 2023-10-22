import sqlite3 #Importamos la librería sqlite3

miConexion=sqlite3.connect("PrimeraBaseDatos") #Creamos y establecemos conexión con nuestra base de datos

miCursor=miConexion.cursor() #Creamos un puntero o cursor 

# Creamos una table con una serie de parámetros y una vez ejecutada, la comentamos para que no nos de error
miCursor.execute("CREATE TABLE PRODUCTOS1 (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS1 VALUES('BALÓN', 15, 'DEPORTES')") # Insertamos valores a la tabla
miConexion.commit() # Damos la confirmación de que estamos de acuerdo en insertar valores nuevos


miConexion.close()
