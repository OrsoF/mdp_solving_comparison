from solvers.gurobi import g_pl as gurobi_pl
from solvers.gurobi import g_pl_dual as gurobi_pl_dual
solve_methods = ['gurobi_pl', 'gurobi_pl_dual']

from solvers.solvers import solve

import pandas as pd
from environments.envs import make_env, envs_list
envs_list = envs_list
import numpy as np

n_exp = 5

building_times = {}
runtimes = {}
for i in range(len(solve_methods)):
    sol = solve_methods[i]
    building_times[sol] = {}
    runtimes[sol] = {}
    for j in range(len(envs_list)):
        env_name = envs_list[j]
        building_times[sol][env_name] = 0
        runtimes[sol][env_name] = 0
        env = make_env(env_name)

        for i in range(n_exp):
            times = solve(env, sol)
            building_times[sol][env_name] += times[0]
            runtimes[sol][env_name] += times[1]
            
        building_times[sol][env_name] /= n_exp
        runtimes[sol][env_name] /= n_exp

func = lambda x : np.round(1000*x, 2)

df_build, df_times = pd.DataFrame(building_times).transpose().apply(func), pd.DataFrame(runtimes).transpose().apply(func)

df_build.to_csv('build_gurobi.csv')
df_times.to_csv('times_gurobi.csv')