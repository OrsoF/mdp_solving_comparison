import importlib
import os
import util

file_list = os.listdir(os.path.join(os.getcwd(), 'solvers'))
try:
    file_list.remove('init.py')
    file_list.remove('pyMarmoteMDP.py')
    file_list.remove('_pyMarmoteMDP.so')
    file_list.remove('__pycache__')
except:
    pass
all_solver_list = ['solvers.'+elem[:-3] for elem in file_list]
solver_list = util.select_solvers(all_solver_list)

def get_solver(solver_name):
    return importlib.import_module(solver_name).Solver
