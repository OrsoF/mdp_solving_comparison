import numpy as np
import pandas as pd

from environments.__init__ import envs_list, make_env
from solvers.__init__ import solver_list, get_solver

env_dim, solver_dim = len(envs_list), len(solver_list)
results = np.zeros((env_dim, solver_dim, 2))

n_exp = 2

for i_env, env_name in enumerate(envs_list):
    for i_solver, solver_name in enumerate(solver_list):
        # print(env_name[13:], solver_name[8:], env.A, env.S)
        for _ in range(n_exp):
            env = make_env(env_name)()
            try:
                solver = get_solver(solver_name)(env)
                results[i_env, i_solver] += solver.building_time, solver.runtime
            except:
                print('Failed :', env_name, solver_name)
                results[i_env, i_solver] += np.nan, np.nan
            

results = results/n_exp



table_dict_build = {}
table_dict_build['Env'] = [elem[13:] for elem in envs_list]
for i_solver, solver in enumerate(solver_list):
    table_dict_build[solver[8:]] = results[:, i_solver, 0]
res_df_build = pd.DataFrame(table_dict_build)

table_dict_solve = {}
table_dict_solve['Env'] = [elem[13:] for elem in envs_list]
for i_solver, solver in enumerate(solver_list):
    table_dict_solve[solver[8:]] = results[:, i_solver, 1]
res_df_solve = pd.DataFrame(table_dict_solve)


print()
print('On {} steps,'.format(n_exp))
print()
print('Average building times :')
print()
print(res_df_build)

print()
print('Average solving times :')
print()
print(res_df_solve)

# Debug

# from solvers.gurobi import Solver
# from environments.taxi import MdpEnv

# env = MdpEnv()
# print(env)
# solver = Solver(env)