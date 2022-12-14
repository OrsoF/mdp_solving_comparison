import numpy as np

class Mdp:
    def __init__(self) -> None:
        self.P = np.array(( ((0,0.6,0.4,0,0,0,0,0,0),
                             (0,1,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,0,1,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((0,0,0,0.3,0.5,0.2,0,0,0),
                             (0,1,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,0,1,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((0,0,0,0,0,0,0.15,0.85,0),
                             (0,1,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,0,1,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((1,0,0,0,0,0,0,0,0),
                             (1,0,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (1,0,0,0,0,0,0,0,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((1,0,0,0,0,0,0,0,0),
                             (0,0,0,0,0,0,0,0,1),
                             (0,0,0,0,0,0,0,0,1),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,0,1,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((1,0,0,0,0,0,0,0,0),
                             (0,1,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,0,0,0,0,0,1),
                             (0,0,0,0,0,0,0,0,1),
                             (0,0,0,0,0,0,0,0,1),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,0,1,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((1,0,0,0,0,0,0,0,0),
                             (0,1,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,0,0,1),
                             (0,0,0,0,0,0,0,1,0),
                             (0,0,0,0,0,0,0,0,1)),
                            ((1,0,0,0,0,0,0,0,0),
                             (0,1,0,0,0,0,0,0,0),
                             (0,0,1,0,0,0,0,0,0),
                             (0,0,0,1,0,0,0,0,0),
                             (0,0,0,0,1,0,0,0,0),
                             (0,0,0,0,0,1,0,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,1,0,0),
                             (0,0,0,0,0,0,0,0,1))))
        pen = 10**7
        self.R = np.array((((15, 10, 5, pen, pen, pen, pen, pen),
                            (pen, pen, pen, 10, 30, pen, pen, pen), 
                            (pen, pen, pen, pen, 15, pen, pen, pen), 
                            (pen, pen, pen, pen, pen, 10, pen, pen),  
                            (pen, pen, pen, pen, pen, 20, pen, pen),
                            (pen, pen, pen, pen, pen, 60, pen, pen),
                            (pen, pen, pen, pen, pen, pen, 5, pen), 
                            (pen, pen, pen, 5, pen, pen, pen, 15),
                            (pen, pen, pen, pen, 0, pen, pen, 0))))
        self.R = self.R.astype(float)
        self.P = self.P.astype(float)
        self.S = 9
        self.A = 8
        self.gamma = 0.999
        self.epsi = 1e-2
        self.__name__ = 'Ex31'