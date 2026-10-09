import numpy as np


class Screen:

    canvas = None
    dimensions = None

    def __init__(self, dimensions: tuple[int, int]):
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

    def draw(self, pos: tuple[int, int], pixels: np.ndarray):
        x, y = pos
        h, w = pixels.shape[:2]
        region = self.canvas[y:y+h, x:x+w]
        rgb = pixels[..., :3]
        alpha = pixels[..., 3:4] / 255.0
        region[:] = np.rint(rgb * alpha + region * (1 - alpha)).astype(int)
