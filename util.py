import gurobipy as grb
import platform
import os
import pickle
import pandas as pd

# import solvers
# import environments
# solv_init = solvers.init
# envs_init = environments.init

def gurobi_license():
    grb.Env('gurobi.log')
    f = open("gurobi.log", "r")
    log = f.read()
    f.close()
    os.remove(os.path.join(os.getcwd(), "gurobi.log"))
    return 'Restricted' not in log

def linux():
    return platform.system() == 'Linux'

def select_solvers(solver_list):
    # if not gurobi_license():
    #     solver_list.remove('solvers.gurobi')
    if not linux():
        solver_list.remove('solvers.marmote')
    return solver_list

def pickle_save(path, file):
    with open(path, 'wb') as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)

def pickle_open(path):
    with open(path, 'rb') as handle:
        file = pickle.load(handle)
    return file

results_files = os.listdir(os.path.join(os.getcwd(), 'results'))

def show_results():
    table_dict_build, table_dict_run = {}, {}
    table_dict_build['Env'], table_dict_run['Env'] = envs_init.envs_list, envs_init.envs_list
    # Res columns
    res = os.listdir(os.path.join(os.getcwd(), 'results'))
    for elem in res:
        file_path = os.path.join(os.getcwd(), 'results', elem)
        res = pickle_open(file_path)
        if 'build' in elem:
            table_dict_build[elem[8:-13]] = res
        else:
            table_dict_run[elem[8:-8]] = res

    res_df_build = pd.DataFrame(table_dict_build)
    res_df_run = pd.DataFrame(table_dict_run)
    print()
    print(res_df_build.style.to_latex())
    print()
    print(res_df_run.style.to_latex())
    print()
    print(res_df_build)
    print()
    print(res_df_run)
