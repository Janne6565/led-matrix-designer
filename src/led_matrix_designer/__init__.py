from .types import Screen


def main() -> None:
    screen = Screen((32, 32))
    screen.fill((255, 0, 0))
    screen.draw_rect((10, 10), (20, 20), (0, 255, 0))
    screen.print()
    print("Hello from led-matrix-designer!")
