import pygame as pg


from game.game_objs.game_obj import GameObj
from utils.constants import *


class Bird(GameObj):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y, width, height)
        self.surface.fill(Colours.white)
        self.y_velocity = 0

    def jump(self) -> None:
        self.y_velocity = -5
