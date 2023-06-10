from game.game_objs.game_obj import GameObj
from utils.constants import *


class GamePipe(GameObj):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(
            x=x,
            y=y,
            width=width,
            height=height,
        )
        self.x_velocity = GameConsts.pipe_speed

        self.surface.fill(Colours.green)
