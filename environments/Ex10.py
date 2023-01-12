import numpy as np

class Mdp:
    def __init__(self) -> None:
        self.S = 2
        self.A = 2
        self.P = np.array([[[0.6, 0.4], [0.5, 0.5]], 
                           [[0.2, 0.8], [0.7, 0.3]]])
        self.R = np.array([[4.5, 2], [-1.5, 3]])
        self.gamma = 0.999
        self.epsi = 1e-2
        self.__name__ = 'Ex10'