import numpy as np
from typing import Callable

INITIAL_RANDOMNESS = 0.3


class Layer:
    def __init__(self, n_inputs: int, n_neurons: int, activation_function: str) -> None:
        # Initialising the weights at random values while keeping them in a reasonable range
        self.weights = self._random_values_in_range(
            range=(-1, 1), shape=(n_inputs, n_neurons)
        )
        self.biases = np.zeros(n_neurons)

        self.activation_function: Callable = ActivationFunctions.get_function(
            activation_function
        )

    def forward(self):
        pass

    def _random_values_in_range(
        self, range: tuple(int, int), shape: tuple
    ) -> np.ndarray:
        """
        Generates an ndarray with shape $shape, filled with random values
        according to the INITIAL_RANDOMNESS constants and the range parameter

        range: tuple[int, int] | Dictates whats the allowed range of values
                    in the matrix, first value is minimum, second is maximum
        """
        values = np.maximum(
            np.minimum(
                INITIAL_RANDOMNESS * np.random.randn(shape),
                range[1],
            ),
            range[0],
        )
        return values


class ActivationFunctions:
    @staticmethod
    def get_function(activation_func: str):
        match activation_func:
            case "None":
                return lambda x: x
            case "ReLu":
                return ActivationFunctions.ReLu
            case "softmax":
                return ActivationFunctions.softmax

    @staticmethod
    def ReLu(neuron_values: np.ndarray):
        return np.maximum(neuron_values, 0)

    @staticmethod
    def softmax(neuron_values: np.ndarray):
        exp_values = np.exp(neuron_values - np.max(neuron_values))
        probabilities = exp_values / np.sum(exp_values)
        return probabilities
