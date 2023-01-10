from mdptoolbox.mdp import ValueIteration, PolicyIteration, ValueIterationGS, PolicyIterationModified
from time import thread_time_ns as thread_time
import numpy as np

class Solver:
    def __init__(self, env, method='vi'):
        self.available_methods = ['vi', 'vigs', 'pi', 'pim']
        assert method in self.available_methods
        self.building_time, self.runtime = 0, 0
        self.env = env
        self.epsi = self.env.epsi
        self.method = method

    def build(self):
        start_time = thread_time()
        if self.method == 'vi':
            self.model = ValueIteration(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi)
        elif self.method=='vigs':
            self.model = ValueIterationGS(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi)
        elif self.method=='pi':
            self.model = PolicyIteration(self.env.P, self.env.R, discount=self.env.gamma)
        elif self.method=='pim':
            self.model = PolicyIterationModified(self.env.P, self.env.R, discount=self.env.gamma)
        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.model.run()
        self.total_time = (thread_time()-start_run_time)+self.building_time
    