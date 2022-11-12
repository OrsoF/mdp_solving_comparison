from environments.example import mdp_env

env = mdp_env()

from solvers.marmote import MarmoteSolver

solver = MarmoteSolver(env)
print('Done')