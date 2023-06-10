class ScreenConsts:
    width = 600
    height = 900
    fps = 60


class BirbConsts:
    width = 20
    height = 20


class GameConsts:
    gravity = -0.3

    pipe_speed = -2
    pipe_width = 50
    pipe_gap = 150
    pipe_min_height = 100

    frames_between_pipes = 2 * ScreenConsts.fps


class Colours:
    white = (255, 255, 255)
    black = (0, 0, 0)
    green = (30, 200, 30)
