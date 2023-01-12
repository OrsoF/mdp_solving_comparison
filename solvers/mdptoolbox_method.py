from mdptoolbox.mdp import ValueIteration, PolicyIteration, ValueIterationGS, PolicyIterationModified
from time import thread_time_ns as thread_time
import numpy as np

class MdpTBSolverVI:
    def __init__(self, env):
        self.building_time, self.runtime = 0, 0
        self.env = env
        self.epsi = 1e-2
        self.max_iter = 1000
        self.__name__ = 'MdpTBSolverVI'

    def build(self):
        start_time = thread_time()
        self.model = ValueIteration(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi, max_iter=self.max_iter)
        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.model.run()
        self.total_time = (thread_time()-start_run_time)+self.building_time
        self.V = np.array(self.model.V)-self.model.V[0]
    
class MdpTBSolverVIGS:
    def __init__(self, env):
        self.building_time, self.runtime = 0, 0
        self.env = env
        self.epsi = 1e-2
        self.max_iter = 1000
        self.__name__ = 'MdpTBSolverVIGS'

    def build(self):
        start_time = thread_time()
        self.model = ValueIterationGS(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi, max_iter=self.max_iter)
        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.model.run()
        self.total_time = (thread_time()-start_run_time)+self.building_time
        self.V = np.array(self.model.V)-self.model.V[0]
    
class MdpTBSolverPI:
    def __init__(self, env):
        self.building_time, self.runtime = 0, 0
        self.env = env
        self.epsi = 1e-2
        self.max_iter = 1000
        self.__name__ = 'MdpTBSolverPI'

    def build(self):
        start_time = thread_time()
        self.model = PolicyIteration(self.env.P, self.env.R, discount=self.env.gamma, max_iter=self.max_iter)
        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.model.run()
        self.total_time = (thread_time()-start_run_time)+self.building_time
        self.V = np.array(self.model.V)-self.model.V[0]
    
class MdpTBSolverPIM:
    def __init__(self, env):
        self.building_time, self.runtime = 0, 0
        self.env = env
        self.epsi = 1e-2
        self.max_iter = 1000
        self.__name__ = 'MdpTBSolverPIM'

    def build(self):
        start_time = thread_time()
        self.model = PolicyIterationModified(self.env.P, self.env.R, discount=self.env.gamma, epsilon=self.epsi, max_iter=self.max_iter)
        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.model.run()
        self.total_time = (thread_time()-start_run_time)+self.building_time
        self.V = np.array(self.model.V)-self.model.V[0]
    