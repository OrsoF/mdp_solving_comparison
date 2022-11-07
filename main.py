from environments.Ex30 import mdp_env

env = mdp_env()

print(env.P.shape)
print(env.R.shape)
print(env.S)
print(env.A)
print(env.P.dtype)

from solvers.marmote import MarmoteSolver

solver = MarmoteSolver(env)
print('Done')