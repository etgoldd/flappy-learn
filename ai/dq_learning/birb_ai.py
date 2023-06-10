import numpy as np

from ai.dq_learning.layer import Layer
from ai.input_generator import InputGenerator
from game.game_environment import GameEnv


INPUT_NEURONS = 2
LAYER1_NEURONS = 4


class BirbAi:
    def __init__(self) -> None:
        self.input_layer = None
