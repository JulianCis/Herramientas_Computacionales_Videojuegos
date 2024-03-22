"""Memory, puzzle game of number pairs.
Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

"""Este código es una implementación del juego memorama."""
"""Al dar click a un recuadro, desbloqueas un número, si encuentras dos numeros iguales, desbloquearas la imagen."""

from random import *
from turtle import *

from freegames import path

"""Define variables para cargar una imagen, generar las fichas del juego, mantener el estado del juego, y controlar la visibilidad de las fichas."""

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan']


car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
taps = 0

def square(x, y):
    """Dibuja un cuadrado blanco con un borde negro en una posición específica (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convertir las coordenadas (x, y) a un índice de ficha en la lista de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte el número de ficha en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza el estado del juego y revela fichas cuando el jugador hace clic en una posición.."""

    global taps
    taps += 1
    print("Numero de taps: ", taps)

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Dibuja la imagen del juego y las fichas en la pantalla para  actualizarlas continuamente.."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        x_offset = x + 25
        y_offset = y + 7
        goto(x_offset, y_offset)
        color(choice(colors))
        write(tiles[mark], align="center", font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

"""Inicializa el juego mezclando las fichas, agregando la imagen del juego, habilitando la captura de clics del mouse, dibujando el juego y finalizando el programa."""
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()