"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

"""
Es un juego donde el jugador debe golpear objetivos con proyectiles disparados desde un cañón.
"""

from random import randrange
from turtle import *

from freegames import vector

# Se inicializan valores
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """El cañón dispara un proyectil en la dirección del clic.
       La velocidad del proyectil se calcula en función de la posición del clic."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25


def inside(xy):
    """Regresa True, si un punto está dentro de los límites de la pantalla."""
    return -200 < xy.x < 200 and -200 < xy.y < 200


def draw():
    """Dibuja las pelotas y los objetivos."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()


def move():
    """Mover los objetos pelota y los objetivos.
       mueve los objetivos hacia la izquierda en la pantalla y aplica la gravedad al proyectil.
       Si un objetivo está lo suficientemente cerca del proyectil,
       se elimina de la lista de objetivos, lo que indica que ha sido golpeado."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

        if not inside(target):
            target.x = 200
            target.y = randrange(-150, 150)

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    ontimer(move, 50)

# Configuración inicial 
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
