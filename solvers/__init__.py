import importlib

solver_list = ['gurobi', 'marmote', 'mdptoolbox_method']
solver_list = ['solvers.'+elem for elem in solver_list]

def get_solver(solver_name):
    return importlib.import_module(solver_name).Solver