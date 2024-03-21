"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

"""Este código es una implementación simple del juego clásico Snake donde cada vez que te acercas a un bloque de color, la serpiente aumentará su tamaño y el bloque de color cambiará de posición"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

colores = ['blue', 'green', 'yellow', 'orange', 'purple']

color_serpiente = choice(colores)
colores.remove(color_serpiente)
color_comida = choice(colores)


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambia la dirección de la serpiente en el eje x y en el eje y."""
    aim.x = x
    aim.y = y


def inside(head):
    """La función regresa verdadero mientras la cabeza de la serpiente esté dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Mueve la serpiente hacia adelante un segmento por movimiento."""
    head = snake[-1].copy()
    head.move(aim)
	
    """Si detecta que la cabeza de la serpiente colisionó, cambia de color a rojo"""
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    """Si la cabeza de la serpiente se encuentra con la comida, aumenta el tamaño del cuerpo de la serpiente"""
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    if randrange(25) == 0:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

    clear()

    """Indica el color del cuerpo de la serpiente"""
    for body in snake:
        square(body.x, body.y, 9, color_serpiente)

    """Indica el color y la posición de la comida"""
    square(food.x, food.y, 9, color_comida)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
"""Las flechas indican la dirección de la serpiente"""
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
