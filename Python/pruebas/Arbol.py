import turtle

# Definimos los colores del árbol
colores = ["brown", "green", "yellow"]

# Creamos una tortuga
t = turtle.Turtle()

# Establecemos el modo de color
from turtle import colormode
colormode(255)

# Dibujamos el tronco
t.pencolor(colores[0])
t.forward(100)

# Dibujamos las ramas
for i in range(4):
    t.pencolor(colores[1])
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)

# Dibujamos las hojas
t.pencolor(colores[2])
t.begin_fill()
for i in range(36):
    t.circle(10)
    t.left(10)
t.end_fill()

# Mostramos el dibujo
turtle.done()
