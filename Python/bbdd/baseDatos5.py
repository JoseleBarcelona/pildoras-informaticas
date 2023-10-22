import sqlite3

miConexion = sqlite3.connect("GestionProductos2")

miCursor = miConexion.cursor()

# miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confección'")
# Lee la totalidad del registro de dicha seccion

# miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")
# Actualizamos un parámetro o varios

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")
# Borramos un registro a través del ID en este caso

productos=miCursor.fetchall()
print(productos)

miConexion.commit()
miConexion.close()
