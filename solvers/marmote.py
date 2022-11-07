from solvers.pyMarmoteMDP import marmoteInterval, sparseMatrixVector, sparseMatrix, discountedMDP

class MarmoteSolver:
    def __init__(self, env, epsi=0.0001, max_iter=1000, method = 'value_iteration'):
        self.env = env
        self.gamma = self.env.gamma
        self.action_space = marmoteInterval(0, self.env.S-1)
        self.state_space = marmoteInterval(0, self.env.A-1)
        self.transition_matrix = sparseMatrixVector(self.env.A)

        for action in range(self.env.A):
            P = sparseMatrix(self.env.S, self.env.S)
            for s1 in range(self.env.S):
                transitions = self.env.P[action, s1]
                for s2, proba in enumerate(transitions):
                    P.addToEntry(s1, s2, proba)
            self.transition_matrix[action] = P

        self.reward_matrix = sparseMatrix(self.env.S, self.env.A)
        for s in range(self.env.S):
            for a in range(self.env.A):
                reward = self.env.R[s, a]
                self.reward_matrix.addToEntry(s, a, reward)

        self.model = discountedMDP('max', 
                                   self.state_space, 
                                   self.action_space, 
                                   self.transition_matrix, 
                                   self.reward_matrix, 
                                   self.gamma)

        if method == 'value_iteration':
            self.optimum = self.model.valueIteration(epsi, max_iter)
        elif method == 'policy_iteration':
            self.model.policyIterationModified(epsi, max_iter, self.gamma, max_iter)
            print('ok')
