import numpy as np

class mdp_env:
    def __init__(self) -> None:

        # Construction de la matrice de transition
        self.P = np.zeros((3, 4, 4))
        self.P[0, 0, 1], self.P[0, 0, 2], self.P[0, 0, 3] = 7/8, 1/16, 1/16
        self.P[0, 1, 1], self.P[0, 1, 3] = 3/4, 1/4
        self.P[0, 2, 2], self.P[0, 2, 3] = 1/2, 1/2
        self.P[0, 3, 3] = 1.

        self.P[1, 0, 0] = 7/8
        self.P[1, 0, 2] = 1/8

        self.P[1, 1, 1] = 3/4
        self.P[1, 1, 2] = 1/8
        self.P[1, 1, 3] = 1/8

        self.P[1, 2, 0] = 8/10
        self.P[1, 2, 2] = 2/10

        self.P[1, 3, 3] = 1.
        self.P[2, 0, 2] = 1.
        self.P[2, 1, 0] = 1.
        self.P[2, 2, 1] = 1.
        self.P[2, 3, 3] = 1.

        # Matrice de Reward
        self.R = np.array([[0., 4000., 6000.],
                           [1000., 4000., 6000.],
                           [3000., 4000., 6000.],
                           [3000., 4000., 6000.]])

        self.gamma = 0.9999
        self.S = 4
        self.A = 3

env = mdp_env()

from solvers.pyMarmoteMDP import marmoteInterval, sparseMatrixVector, sparseMatrix, discountedMDP

class MarmoteSolver:
    def __init__(self, env, epsi=0.0001, max_iter=1000, method = 'value_iteration'):

        # Paramètres
        self.env = env
        self.gamma = self.env.gamma
        self.action_space = marmoteInterval(0, self.env.S-1)
        self.state_space = marmoteInterval(0, self.env.A-1)
        self.transition_matrix = sparseMatrixVector(self.env.A)

        # Matrice de transition
        for action in range(self.env.A):
            P = sparseMatrix(self.env.S, self.env.S)
            for s1 in range(self.env.S):
                transitions = self.env.P[action, s1]
                for s2, proba in enumerate(transitions):
                    P.addToEntry(s1, s2, proba)
            self.transition_matrix[action] = P

        # Matrice de reward
        self.reward_matrix = sparseMatrix(self.env.S, self.env.A)
        for s in range(self.env.S):
            for a in range(self.env.A):
                reward = self.env.R[s, a]
                self.reward_matrix.addToEntry(s, a, reward)

        # Construction du modèle
        self.model = discountedMDP('max', 
                                   self.state_space, 
                                   self.action_space, 
                                   self.transition_matrix, 
                                   self.reward_matrix, 
                                   self.gamma)

        # Résolution
        
        # if method == 'value_iteration':
        #     self.optimum = self.model.valueIteration(epsi, max_iter)
        # elif method == 'policy_iteration':
        #     self.model.policyIterationModified(epsi, max_iter, self.gamma, max_iter)

solver = MarmoteSolver(env)
