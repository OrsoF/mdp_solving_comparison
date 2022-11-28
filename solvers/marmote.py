from solvers.pyMarmoteMDP import marmoteInterval, sparseMatrix, totalRewardMDP
from time import thread_time

class Solver:
    def __init__(self, env, method='vi', epsi=0.0001, max_iter=1000):
        assert method in ['vi', 'vigs', 'pi', 'pim']
        # Paramètres
        self.env = env
        self.gamma = self.env.gamma


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
                    if self.env.P[a, s, s] > 0.:
                        P.addToEntry(s, s, self.env.P[a, s, s])
            self.mdp.addMatrix(a, P)
            self.transitions_list.append(P)
            P = None

        # self.mdp.writeMDP()

        self.building_time = thread_time()-start_time

        if method=='vi':
            self.opt = self.mdp.valueIteration(epsi, max_iter)
        elif method=='vigs':
            self.opt = self.mdp.valueIterationGS(epsi, max_iter)
        elif method=='pi':
            self.opt = self.mdp.policyIteration(epsi, max_iter)
        elif method=='pim':
            self.opt = self.mdp.policyIterationModified(epsi, max_iter)

        self.runtime = thread_time()-self.building_time
        # self.opt.writeSolution()


def m_vi(env):
    solver = Solver(env, 'vi')
    return solver.building_time, solver.runtime

def m_vigs(env):
    solver = Solver(env, 'vigs')
    return solver.building_time, solver.runtime

def m_pi(env):
    solver = Solver(env, 'pi')
    return solver.building_time, solver.runtime

def m_pim(env):
    solver = Solver(env, 'pim')
    return solver.building_time, solver.runtime
