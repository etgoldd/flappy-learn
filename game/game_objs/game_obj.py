import pygame as pg


from utils.constants import *


class GameObj:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y

        self.x_velocity = 0
        self.y_velocity = 0

        self.rect = pg.rect.Rect(
            x,
            y,
            width,
            height,
        )
        self.surface = pg.Surface(size=(width, height))
