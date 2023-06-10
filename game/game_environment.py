import pygame as pg
import random

from game.game_objs.game_obj import GameObj
from game.game_objs.pipe import GamePipe
from game.game_objs.bird import Bird
from utils.constants import *


class GameEnv:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        # tracks the amount of moments that have passed
        self.t = 0
        self.alive = True
        self.birb = Bird(
            x=(self.width - BirbConsts.width) // 2,
            y=(self.height - BirbConsts.height) // 2,
            width=BirbConsts.width,
            height=BirbConsts.height,
        )

        self.pipes: list[GamePipe] = []

        self.game_objs: list[GameObj] = [self.birb, *self.pipes]

        self._add_pipe()

    def _move_game_objs(self):
        for game_obj in self.game_objs:
            game_obj.rect.x += game_obj.x_velocity
            game_obj.rect.y += game_obj.y_velocity

    def _bird_gravity_affect(self):
        self.birb.y_velocity -= GameConsts.gravity

    def _add_pipe(self):
        # Leaves at least pipe_min_height between the top or bottom of the screen
        # to the start of the pipe
        gap_start = random.randrange(
            GameConsts.pipe_min_height,
            self.height - GameConsts.pipe_min_height - GameConsts.pipe_gap,
        )

        top_pipe = GamePipe(
            x=self.width, y=0, width=GameConsts.pipe_width, height=gap_start
        )
        bottom_pipe = GamePipe(
            x=self.width,
            y=gap_start + GameConsts.pipe_gap,
            width=GameConsts.pipe_width,
            height=self.height - gap_start - GameConsts.pipe_gap,
        )

        self.game_objs += top_pipe, bottom_pipe
        self.pipes += top_pipe, bottom_pipe

    def _check_collision(self) -> bool:
        pipe_rects = [pipe.rect for pipe in self.pipes]
        collide = self.birb.rect.collidelist(pipe_rects)
        return False if collide == -1 else True

    def _remove_old_pipes(self):
        old_pipes = []
        for pipe in self.pipes:
            if pipe.rect.x < -GameConsts.pipe_width:
                old_pipes.append(pipe)

        [
            (self.pipes.remove(old_pipe), self.game_objs.remove(old_pipe))
            for old_pipe in old_pipes
        ]

    def birb_jump(self):
        """
        Makes the birb jump
        """
        self.birb.jump()

    def pass_time(self):
        """
        Should be called every frame
        """
        self.t += 1

        # If the bird has collided with a pipe, kill the birb
        self.alive = not self._check_collision()

        # Adding downwards velocity to birb
        self._bird_gravity_affect()

        # moving all the game objects according to their velocity
        self._move_game_objs()

        # If pipes have left the screen, remove them
        self._remove_old_pipes()

        if self.t % GameConsts.frames_between_pipes == 0:
            self._add_pipe()
