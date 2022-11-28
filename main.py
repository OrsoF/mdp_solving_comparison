import pandas as pd
from tqdm import tqdm
from environments.envs import make_env, envs_list
from solvers.solvers import solve, solve_methods

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

df_build, df_times = pd.DataFrame(building_times).transpose(), pd.DataFrame(runtimes).transpose()

print()
print(df_build.style.to_latex())
print()
print(df_times.style.to_latex())

print()
print('Building times')
print()
print(df_build)

print()
print('Run times')
print()
print(df_times)


