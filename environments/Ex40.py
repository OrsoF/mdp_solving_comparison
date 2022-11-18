import numpy as np

class MdpEnv:
    def __init__(self) -> None:
        self.P = P = np.array((((1,0,0,0),(0.75,0.25,0,0 ),(0.25,0.5,0.25,0),(0,0.25,0.5,0.25)), 
                                ((0.75,0.25,0,0),(0.25,0.5,0.25,0 ),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25)), 
                                ((0.25,0.5,0.25,0),(0,0.25,0.5,0.25 ),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25)), 
                                ((0,0.25,0.5,0.25),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25),(0,0.25,0.5,0.25))))
        self.R = np.array(((0, -1, -2, -5), 
                            (5,0 ,-3,-1000),
                            (6,-1,-1000,-1000),
                            (5,-1000,-1000,-1000)))
        self.R = self.R.astype(float)
        self.P = self.P.astype(float)
        self.gamma = 0.999
        self.S = 4
        self.A = 4
