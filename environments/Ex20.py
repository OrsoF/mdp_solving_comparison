import numpy as np

class MdpEnv:
    def __init__(self) -> None:
        self.P = np.zeros((4, 3, 3))
        self.P[0, 0, 2] = 1
        self.P[0, 1, 1] = 1
        self.P[0, 2, 2] = 1
        self.P[1, 0, 1] = 1
        self.P[1, 1, 1] = 1
        self.P[1, 2, 2] = 1
        self.P[2, 0, 0] = 1
        self.P[2, 1, 0] = 1
        self.P[2, 2, 2] = 1
        self.P[3, 0, 1] = 1
        self.P[3, 1, 1] = 1
        self.P[3, 2, 0] = 1/3
        self.P[3, 2, 1] = 1/3
        self.P[3, 2, 2] = 1/3

        self.R = np.zeros((3, 4))

        self.R[0,0] = 2
        self.R[0,1] = 1
        self.R[0,2] = -1000
        self.R[0,3] = -1000

        self.R[1,0] = -1000
        self.R[1,1] = -1000
        self.R[1,2] = 2
        self.R[1,3] = -1000

        self.R[2,0] = -1000
        self.R[2,1] = -1000
        self.R[2,2] = -1000
        self.R[2,3] = 3

        

        self.gamma = 1
        self.S = 3
        self.A = 4