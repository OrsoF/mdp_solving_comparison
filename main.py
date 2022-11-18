import numpy as np
import pandas as pd
import os

from environments import init as envs_init
from solvers import init as solv_init

env_dim, solver_dim = len(envs_init.envs_list), len(solv_init.solver_list)

building_times = {}
runtimes = {}

n_exp = 100

for i_solver, solver_name in enumerate(solv_init.solver_list):
    
    building_times[solver_name] = []
    runtimes[solver_name] = []

    for i_env, env_name in enumerate(envs_init.envs_list):
        build_time, run_time = [], []

        for _ in range(n_exp):
            env = envs_init.make_env('environments.'+env_name[:-3])()
            solver = solv_init.get_solver(solver_name)(env)
            build_time.append(solver.building_time)
            run_time.append(solver.runtime)

        build_time = np.mean(build_time)
        run_time = np.mean(run_time)

        building_times[solver_name].append(build_time)
        runtimes[solver_name].append(run_time)

from util import pickle_save, show_results

results_path = os.path.join(os.getcwd(), 'results')
for solver_name in building_times.keys():
    build_path = os.path.join(results_path, solver_name+'_building.pkl')
    run_path = os.path.join(results_path, solver_name+'_run.pkl')
    pickle_save(build_path, building_times[solver_name])
    pickle_save(run_path, runtimes[solver_name])

show_results()

# table_dict_build = {}
# table_dict_build['Env'] = [elem[13:] for elem in envs_list]
# for i_solver, solver in enumerate(solver_list):
#     table_dict_build[solver[8:]] = results[:, i_solver, 0]
# res_df_build = pd.DataFrame(table_dict_build)

# table_dict_solve = {}
# table_dict_solve['Env'] = [elem[13:] for elem in envs_list]
# for i_solver, solver in enumerate(solver_list):
#     table_dict_solve[solver[8:]] = results[:, i_solver, 1]
# res_df_solve = pd.DataFrame(table_dict_solve)


# print()
# print('On {} steps,'.format(n_exp))
# print()
# print('Average building times :')
# print()
# print(res_df_build)

# print()
# print('Average solving times :')
# print()
# print(res_df_solve)

# res = [res_df_build, res_df_solve]

# 

# with open('res_2.pickle', 'wb') as handle:
#     pickle.dump(res, handle, protocol=pickle.HIGHEST_PROTOCOL)


# # Debug

# # from solvers.gurobi import Solver
# # from environments.taxi import MdpEnv

# # env = MdpEnv()
# # print(env)
# # solver = Solver(env)