from random import randrange
from turtle import *

from freegames import vector

# Se inicializan valores
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
target_speed = 5  # Velocidad de los objetivos
gravity = 1  # Gravedad del proyectil
max_targets = 5  # Máximo número de objetivos en pantalla

def tap(x, y):
    """El cañón dispara un proyectil en la dirección del clic.
       La velocidad del proyectil se calcula en función de la posición del clic."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 5  # Ajusta la velocidad del proyectil en x
        speed.y = (y + 200) / 5  # Ajusta la velocidad del proyectil en y


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
    global targets

    if len(targets) < max_targets and randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    new_targets = []

    for target in targets:
        target.x -= target_speed

        if inside(target):
            new_targets.append(target)

    targets = new_targets

    if inside(ball):
        speed.y -= gravity  # Aplica la gravedad al proyectil
        ball.move(speed)

    new_targets = []

    for target in targets:
        if abs(target - ball) > 13:
            new_targets.append(target)

    targets = new_targets

    draw()

    if not inside(ball):
        ball.x = -200
        ball.y = -200

    ontimer(move, 50)

# Configuración inicial
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
