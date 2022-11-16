from mdptoolbox.mdp import ValueIteration, PolicyIteration
from time import thread_time

class Solver:
    def __init__(self, env, method='value_iteration'):
        self.env = env

        if method == 'value_iteration':
            start_time = thread_time()
            self.model = ValueIteration(self.env.P, self.env.R, discount=self.env.gamma)
        else:
            start_time = thread_time()
            self.model = PolicyIteration(self.env.P, self.env.R, discount=self.env.gamma)

        self.building_time = thread_time()-start_time

        self.model.run()

        self.runtime = thread_time()-self.building_time
