import pygame as pg

from utils.constants import *
from game.game_environment import GameEnv


class GameScene:
    def __init__(self, width: int, height: int, fps: int) -> None:
        self.width = width
        self.height = height
        self.window = pg.display.set_mode((self.width, self.height))

        self.fps = fps

        self.game_env = GameEnv(width, height)

    def blit_screen(self):
        self.window.fill(Colours.black)

        # Blitting all the game objects
        for game_obj in self.game_env.game_objs:
            self.window.blit(source=game_obj.surface, dest=game_obj.rect)

        pg.display.update()

    def make_active_scene(self):
        run = True
        clock = pg.time.Clock()

        while run:
            clock.tick(self.fps)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            self.game_env.pass_time()
            if not self.game_env.alive:
                run = False

            keys_pressed = pg.key.get_pressed()

            if keys_pressed[pg.K_SPACE]:
                self.game_env.birb_jump()
            if keys_pressed[pg.K_ESCAPE]:
                run = False

            self.blit_screen()


if __name__ == "__main__":
    scene = GameScene(
        width=ScreenConsts.width,
        height=ScreenConsts.height,
        fps=ScreenConsts.fps,
    )
    scene.make_active_scene()
    pg.quit()
