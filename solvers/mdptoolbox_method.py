from mdptoolbox.mdp import ValueIteration, PolicyIteration, ValueIterationGS, PolicyIterationModified
from time import thread_time_ns as thread_time
import numpy as np

class Solver:
    def __init__(self, env, method='vi'):

        assert method in ['vi', 'vigs', 'pi', 'pim']
        self.building_time, self.runtime = 0, 0
        self.env = env
        self.epsi = self.env.epsi

        if method == 'vi':
            start_time = thread_time()
            self.model = ValueIteration(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi)
        elif method=='vigs':
            start_time = thread_time()
            self.model = ValueIterationGS(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi)
        elif method=='pi':
            start_time = thread_time()
            self.model = PolicyIteration(self.env.P, self.env.R, discount=self.env.gamma)
        elif method=='pim':
            start_time = thread_time()
            self.model = PolicyIterationModified(self.env.P, self.env.R, discount=self.env.gamma)

        self.building_time = thread_time()-start_time

        self.model.run()

        self.runtime = thread_time()-start_time-self.building_time

def mtb_vi(env):
    solver = Solver(env, 'vi')
    return solver.building_time + solver.runtime

def mtb_vigs(env):
    solver = Solver(env, 'vigs')
    return solver.building_time + solver.runtime

def mtb_pi(env):
    solver = Solver(env, 'pi')
    return solver.building_time + solver.runtime

def mtb_pim(env):
    solver = Solver(env, 'pim')
    return solver.building_time + solver.runtime
    