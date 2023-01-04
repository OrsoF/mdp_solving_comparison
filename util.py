import gurobipy as grb
import platform
import os
import pickle

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

def check_environment(env):
    assert len(env.P.shape)==3
    assert len(env.R.shape)==2
    assert env.P.shape[1]==env.P.shape[2] and env.P.shape[1]==env.R.shape[0]
    assert env.P.shape[0]==env.R.shape[1]
    assert 0 < env.gamma <= 1
    assert 0 < env.epsi < 1