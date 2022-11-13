import numpy as np
from mdptoolbox.util import check

class MdpEnv:
    def __init__(self, S=100, A=20) -> None:
        self.S, self.A = S, A
        self.P = np.random.random(size=(A, S, S))
        self.P = np.divide(self.P,np.sum(self.P, axis=2)[:, :, np.newaxis])
        self.R = np.random.random(size=(S, A))
        self.gamma = np.random.random()
        check(self.P, self.R)
