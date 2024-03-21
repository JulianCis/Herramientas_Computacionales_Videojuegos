"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""
"""
Este código proporciona una interfaz básica para dibujar formas como líneas, cuadrados y círculos en una ventana gráfica.
Seleccionas la forma y el color con las teclas y el primer click es el punto inicial y el segundo el punto final
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Dibuja la línea de inicio a fin"""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Dibuja un cuadrado de inicio a fin, hacia arriba"""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Dibuja un círculo de inicio a fin. Por implementar."""
    pass  # TODO


def rectangle(start, end):
    """Dibuja un rectángulo de inicio a fin."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    width = end.x - start.x
    height = end.y - start.y

    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


def triangle(start, end):
    """Dibuja un triángulo de inicio a fin."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Guarda el punto inicial o dibujar la figura"""
    start = state['start']

# Guardar el punto inicial
    if start is None:
        state['start'] = vector(x, y)
# Dibujar la figura
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Guardar el valor en estado al código."""
    state[key] = value

# Se define estado inicial y se espera para recibir indicaciones por teclado
state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('gray'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
