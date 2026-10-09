import numpy as np


class Screen:

    canvas = None
    dimensions = None

    def __init__(self, dimensions: tuple):
        self.dimensions = dimensions
        self.canvas = np.zeros((dimensions[0], dimensions[1], 3), dtype=int)

    def print(self):
        for row in self.canvas:
            line = ""
            for pixel in row:
                r, g, b = pixel
                # ANSI-Code für True-Color (24-bit) Hintergrund
                # \x1b[48;2;R;G;Bm färbt den Hintergrund des Leerzeichens
                line += f"\x1b[48;2;{r};{g};{b}m  "
            # Am Zeilenende die Farbe zurücksetzen (\x1b[0m)
            print(line + "\x1b[0m")

    def fill(self, color):
        self.canvas[0:self.dimensions[1], 0:self.dimensions[0]] = color

    def draw_rect(self, pos1, pos2, color):
        self.canvas[pos1[1]:pos2[1], pos1[0]:pos2[0]] = color


class Animatable:
    position = (0, 0)

    def __init__(self):
        raise NameError("Cant instantiate generic")

    def render(self, screen) -> np.array:
        raise NameError("Method not callable on generic")


class Rectangle(Animatable):
    width = 0
    height = 0

    def __init__(self, pos, width, height):
        self.position = pos
        self.width = width
        self.height = height

    def render(self, screen):
        pass
