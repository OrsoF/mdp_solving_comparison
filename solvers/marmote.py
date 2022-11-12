from solvers.pyMarmoteMDP import marmoteInterval, sparseMatrix, totalRewardMDP

class MarmoteSolver:
    def __init__(self, env, epsi=0.0001, max_iter=1000, method = 'value_iteration'):
        print('Building MDP...')
        # Paramètres
        self.env = env
        self.gamma = self.env.gamma

        self.state_space = marmoteInterval(0, self.env.S-1)
        self.action_space = marmoteInterval(0, self.env.A-1)
        self.S = self.state_space.cardinal()
        self.A = self.action_space.cardinal()

        self.reward_matrix = sparseMatrix(self.S, self.A)

        for a in range(self.env.A):
            for s in range(self.env.S):
                self.reward_matrix.addToEntry(s, a, self.env.R[s, a])

        print('Building MDP...')
        self.mdp = totalRewardMDP('min', self.state_space, self.action_space, self.reward_matrix) 

        self.transitions_list = list()

        print('Transition matrix...')
        for a in range(self.env.A):
            P = sparseMatrix(self.S)
            for s1 in range(self.env.S):
                for s2 in range(self.env.S):
                    if self.env.P[a, s, s] > 0.:
                        P.addToEntry(s, s, self.env.P[a, s, s])
            self.mdp.addMatrix(a, P)
            self.transitions_list.append(P)
            P = None

        self.mdp.writeMDP()

        self.opt = self.mdp.valueIteration(epsi, max_iter)
        self.opt.writeSolution()