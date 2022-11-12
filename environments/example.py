import numpy as np
from mdptoolbox.util import check

class mdp_env:
    def __init__(self, S=10, A=10) -> None:
        self.S, self.A = S, A
        self.P = np.random.random(size=(A, S, S))
        self.P = np.divide(self.P,np.sum(self.P, axis=2)[:, :, np.newaxis])
        self.R = np.random.random(size=(S, A))
        self.gamma = np.random.random()
        check(self.P, self.R)
