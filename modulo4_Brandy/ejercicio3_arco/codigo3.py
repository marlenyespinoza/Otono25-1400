# TODO: Usa el código del archivo `codigo2.py` como base para crear una figura diferente.
# Algunas ideas: un arco, un paralelogramo, una estrella, o cualquier otra figura creativa.
import turtle
t =turtle.Turtle
ventana = turtle.Screen()

# este for es para hacer los circulos del centro de la flor
flor = turtle.Turtle()
flor.color("purple") # usamos este for para cambiar el color
for i in range(7):
   flor.circle(100)
   flor.right(60)

# este for es para simular los petalos de nuestra flor
flor.color("yellow") # usamos este for para cambiar el color
for i in range(20):
    flor.circle(30)
    flor.right(80)




