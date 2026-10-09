import numpy as np


class Animatable:
    position = (0, 0)

    def __init__(self):
        raise NameError("Cant instantiate generic")

    def render(self, screen) -> np.ndarray:
        raise NameError("Method not callable on generic")

    def get_position(self) -> tuple[int, int]:
        return self.position


class Rectangle(Animatable):
    width = 0
    height = 0
    color = None
    opacity = None

    def __init__(self, pos: tuple[int, int], width: int, height: int, color: tuple[int, int], opacity: int):
        self.position = pos
        self.width = width
        self.height = height
        self.color = color
        self.opacity = opacity

    def render(self) -> np.ndarray:
        return np.full((self.width, self.height, 4), (self.color[0], self.color[1], self.color[2], self.opacity), dtype=int)


class Shape(Animatable):
    shape = None
    color = None
    opacity = None

    def __init__(self, pos: tuple[int, int], shape: np.ndarray, color: tuple[int, int, int], opacity: int):
        self.position = pos
        self.shape = shape
        self.color = color
        self.opacity = opacity

    def render(self) -> np.ndarray:
        h, w = self.shape.shape
        pixels = np.zeros((h, w, 4), dtype=int)
        pixels[..., :3] = self.color
        pixels[..., 3] = np.rint(self.shape / 255 * self.opacity)
        return pixels
