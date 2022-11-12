from environments.__init__ import envs_list, make_env

env_name = envs_list[-1]

env = make_env(env_name)(100, 1000)

from solvers.mdptoolbox_method import Solver

solver = Solver(env)
print(solver.building_time, solver.runtime)