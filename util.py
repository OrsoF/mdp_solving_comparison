import gurobipy as grb
import platform
import os
import pickle
from mdptoolbox.util import check
import gym
import numpy as np

def gurobi_license():
    grb.Env('gurobi.log')
    f = open("gurobi.log", "r")
    log = f.read()
    f.close()
    os.remove(os.path.join(os.getcwd(), "gurobi.log"))
    return 'Restricted' not in log

def linux():
    return platform.system() == 'Linux'

def select_solvers(solver_list):
    # if not gurobi_license():
    #     solver_list.remove('solvers.gurobi')
    if not linux():
        solver_list.remove('solvers.marmote')
    return solver_list

def pickle_save(path, file):
    with open(path, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)

def pickle_open(path):
    with open(path, 'rb') as handle:
        file = pickle.load(handle)
    return file

def check_environment(env):
    assert len(env.P.shape)==3
    assert len(env.R.shape)==2
    assert env.P.shape[1]==env.P.shape[2]==env.R.shape[0]==env.S
    assert env.P.shape[0]==env.R.shape[1]==env.A
    assert 0 < env.gamma <= 1
    assert 0 < env.epsi < 1
    check(env.P, env.R)

class MdpGym:
    def __init__(self, gym_env_name) -> None:
        self.env = gym.make("Taxi-v3")
        self.S = self.env.observation_space.n
        self.A = self.env.action_space.n
        self.P = np.zeros((self.A, self.S, self.S))
        for a in range(self.A):
            for i in range(self.S):   
                liste = self.env.P[i][a] 
                for tup in liste:
                    self.P[a][i,tup[1]] = self.P[a][i,tup[1]] + tup[0]

        self.R = np.zeros((self.S, self.A))
        for s in range(self.S):
            for a in range(self.A):
                liste = self.env.P[s][a]
                for tup in liste:
                    self.R[s,a] = self.R[s,a] + tup[2]

def compute_policy(P, R, V):
    pass

def compute_value(P, R, policy):
    pass