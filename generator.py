import numpy as np

class Generator:
    def __init__(self, seed=None):
        self._random_state = np.random.RandomState(seed)

    def uniform(self, low=0.0, high=1.0, size=None):
        if size is None:
            return low + (high - low) * self._random_state.random_sample()
        else:
            return low + (high - low) * self._random_state.random_sample(size)