from solvers.pyMarmoteMDP import marmoteInterval, sparseMatrix, totalRewardMDP
from time import thread_time_ns as thread_time

class MarmoteSolverVI:
    def __init__(self, env):
        # Paramètres
        self.env = env
        self.gamma = self.env.gamma
        self.epsi = self.env.epsi
        self.max_iter = 1000
        self.__name__ = 'MarmoteSolverVI'

    def build(self):
        start_time = thread_time()
        self.state_space = marmoteInterval(0, self.env.S-1)
        self.action_space = marmoteInterval(0, self.env.A-1)
        self.S = self.state_space.cardinal()
        self.A = self.action_space.cardinal()
        self.reward_matrix = sparseMatrix(self.S, self.A)
        for a in range(self.env.A):
            for s in range(self.env.S):
                self.reward_matrix.addToEntry(s, a, self.env.R[s, a])
        self.mdp = totalRewardMDP('min', self.state_space, self.action_space, self.reward_matrix) 
        self.transitions_list = list()
        for a in range(self.env.A):
            P = sparseMatrix(self.S)
            for s1 in range(self.env.S):
                for s2 in range(self.env.S):
                    if self.env.P[a, s1, s2] > 0.:
                        P.addToEntry(s1, s2, self.env.P[a, s1, s2])
            self.mdp.addMatrix(a, P)
            self.transitions_list.append(P)
            P = None

        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.opt = self.mdp.valueIteration(self.epsi, self.max_iter)
        self.total_time = (thread_time()-start_run_time)+self.building_time

class MarmoteSolverVIGS:
    def __init__(self, env):
        # Paramètres
        self.env = env
        self.gamma = self.env.gamma
        self.epsi = self.env.epsi
        self.max_iter = 1000
        self.__name__ = 'MarmoteSolverVIGS'

    def build(self):
        start_time = thread_time()

        self.state_space = marmoteInterval(0, self.env.S-1)
        self.action_space = marmoteInterval(0, self.env.A-1)
        self.S = self.state_space.cardinal()
        self.A = self.action_space.cardinal()
        self.reward_matrix = sparseMatrix(self.S, self.A)
        for a in range(self.env.A):
            for s in range(self.env.S):
                self.reward_matrix.addToEntry(s, a, self.env.R[s, a])
        self.mdp = totalRewardMDP('min', self.state_space, self.action_space, self.reward_matrix) 
        self.transitions_list = list()
        for a in range(self.env.A):
            P = sparseMatrix(self.S)
            for s1 in range(self.env.S):
                for s2 in range(self.env.S):
                    if self.env.P[a, s1, s2] > 0.:
                        P.addToEntry(s1, s2, self.env.P[a, s1, s2])
            self.mdp.addMatrix(a, P)
            self.transitions_list.append(P)
            P = None

        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.opt = self.mdp.valueIterationGS(self.epsi, self.max_iter)
        self.total_time = (thread_time()-start_run_time)+self.building_time

class MarmoteSolverPI:
    def __init__(self, env):
        # Paramètres
        self.env = env
        self.gamma = self.env.gamma
        self.epsi = self.env.epsi
        self.max_iter = 1000
        self.__name__ = 'MarmoteSolverPI'

    def build(self):
        start_time = thread_time()

        self.state_space = marmoteInterval(0, self.env.S-1)
        self.action_space = marmoteInterval(0, self.env.A-1)
        self.S = self.state_space.cardinal()
        self.A = self.action_space.cardinal()
        self.reward_matrix = sparseMatrix(self.S, self.A)
        for a in range(self.env.A):
            for s in range(self.env.S):
                self.reward_matrix.addToEntry(s, a, self.env.R[s, a])
        self.mdp = totalRewardMDP('min', self.state_space, self.action_space, self.reward_matrix) 
        self.transitions_list = list()
        for a in range(self.env.A):
            P = sparseMatrix(self.S)
            for s1 in range(self.env.S):
                for s2 in range(self.env.S):
                    if self.env.P[a, s1, s2] > 0.:
                        P.addToEntry(s1, s2, self.env.P[a, s1, s2])
            self.mdp.addMatrix(a, P)
            self.transitions_list.append(P)
            P = None
        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.opt = self.mdp.policyIteration(self.max_iter)
        self.total_time = (thread_time()-start_run_time)+self.building_time

class MarmoteSolverPIM:
    def __init__(self, env):
        # Paramètres
        self.env = env
        self.gamma = self.env.gamma
        self.epsi = self.env.epsi
        self.max_iter = 1000
        self.__name__ = 'MarmoteSolverPIM'

    def build(self):
        start_time = thread_time()

        self.state_space = marmoteInterval(0, self.env.S-1)
        self.action_space = marmoteInterval(0, self.env.A-1)
        self.S = self.state_space.cardinal()
        self.A = self.action_space.cardinal()
        self.reward_matrix = sparseMatrix(self.S, self.A)
        for a in range(self.env.A):
            for s in range(self.env.S):
                self.reward_matrix.addToEntry(s, a, self.env.R[s, a])
        self.mdp = totalRewardMDP('min', self.state_space, self.action_space, self.reward_matrix) 
        self.transitions_list = list()
        for a in range(self.env.A):
            P = sparseMatrix(self.S)
            for s1 in range(self.env.S):
                for s2 in range(self.env.S):
                    if self.env.P[a, s1, s2] > 0.:
                        P.addToEntry(s1, s2, self.env.P[a, s1, s2])
            self.mdp.addMatrix(a, P)
            self.transitions_list.append(P)
            P = None

        self.building_time = thread_time() - start_time

    def run(self):
        start_run_time = thread_time()
        self.opt = self.mdp.policyIterationModified(self.epsi, self.max_iter, self.epsi, self.max_iter)
        self.total_time = (thread_time()-start_run_time)+self.building_time
