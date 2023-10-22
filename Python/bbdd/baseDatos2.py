import sqlite3 

miConexion=sqlite3.connect("PrimeraBaseDatos") 

miCursor=miConexion.cursor() 

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balón', 15, 'Deportes')") # Insertamos valores a la tabla

variosProductos=[

    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90, "Cerámica"),
    ("Camión", 20, "Juguetería")

]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
# los tres ?,?,? es uno por cada campo

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos2=miCursor.fetchall()
print(variosProductos2)

for productos in variosProductos2:
    print(productos)
    print("Nombre artículo: ", productos[0], "Nombre sección: ", productos[2])


miConexion.commit()
miConexion.close()
