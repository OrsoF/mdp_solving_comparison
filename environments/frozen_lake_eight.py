import gym
import numpy as np
from mdptoolbox.util import check

env = gym.make("FrozenLake8x8-v1")

def build_P_frozen_lake(A, S):
    P = np.zeros((A, S, S))
    for a in range(A):
        for i in range(S):   
            liste = env.P[i][a] 
            for tup in liste:
                P[a][i,tup[1]] = P[a][i,tup[1]] + tup[0]
    return P

def build_R_frozen_lake(A, S):
    R = np.zeros((S,A))
    for s in range(S):
        for a in range(A):
            liste = env.P[s][a]
            for tup in liste:
            # print(tup)
                R[s,a] = R[s,a] + tup[2]
    return R

class MdpEnv:
    def __init__(self) -> None:
        self.S = 64
        self.A = 4
        self.P = build_P_frozen_lake(self.A, self.S)
        self.R = build_R_frozen_lake(self.A, self.S)
        self.gamma = 0.999
        self.epsi = 1e-5
        