import turtle

# Definimos los colores del arcoíris
colores = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Creamos una tortuga
t = turtle.Turtle()

# Establecemos el modo de color
from turtle import colormode
colormode(255)

# Dibujamos el arcoíris
for color in colores:
    t.pencolor(color)
    t.circle(100)
    t.left(60)

# Mostramos el dibujo
turtle.done()
