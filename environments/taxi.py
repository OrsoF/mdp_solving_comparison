import numpy as np
import gym
from mdptoolbox.util import check

gym_env = gym.make("Taxi-v3")

def build_P_frozen_lake(A, S):
    P = np.zeros((A, S, S))
    for a in range(A):
        for i in range(S):   
            liste = gym_env.P[i][a]  #env.P[0] etat 1, les actions qu on peu faire depuis et leurs détails
            for tup in liste:
                P[a][i,tup[1]] = P[a][i,tup[1]] + tup[0]
    return P

def build_R_frozen_lake(A, S):
    R = np.zeros((S,A))
    for s in range(S):
        for a in range(A):
            liste = gym_env.P[s][a]
            for tup in liste:
                R[s,a] = R[s,a] + tup[2]
    return R

class mdp_env:
    def __init__(self) -> None:
        self.S = gym_env.observation_space.n
        self.A = gym_env.action_space.n
        self.P = build_P_frozen_lake(self.A, self.S)
        self.R = build_R_frozen_lake(self.A, self.S)
        self.gamma = 0.9999