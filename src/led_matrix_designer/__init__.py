import numpy as np
from .screen import Screen
from .animatables import Rectangle, Shape


def main() -> None:
    screen = Screen((32, 32))
    rect = Rectangle((10, 10), 10, 10, (0, 0, 255), 150)
    leaf = Shape(
        (20, 20),
        np.array([[0, 50, 50, 0, 10, 10, 20, 0],
                  [50, 100, 100, 50, 100, 100, 20, 0],
                  [50, 100, 100, 50, 100, 100, 20, 0],
                  [50, 100, 100, 50, 100, 100, 20, 0],
                  [50, 100, 100, 50, 100, 100, 20, 0],
                  [0, 50, 50, 0, 10, 10, 20, 0]]),
        [0, 0, 0],
        255)
    screen.fill((255, 0, 0))
    screen.draw(leaf.position, leaf.render())
    screen.print()
