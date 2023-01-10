from util import gurobi_license
import platform

from envs import MdpEnv
env = MdpEnv()
env.make_env(env.available_envs[0])

available_solvers = {}
from solvers.mdptoolbox_method import Solver as MdpSolver
available_solvers['MdpSolver'] = MdpSolver(env, 'vi').available_methods

if platform.system() == 'Linux':
    from solvers.marmote import Solver as MarmoteSolver
    available_solvers['MarmoteSolver'] = MarmoteSolver(env, 'vi').available_methods
else:
    print('Marmote is not working currently.')

if gurobi_license():
    from solvers.gurobi import Solver as GurobiSolver
    available_solvers['GurobiSolver'] = GurobiSolver(env, 'Pl').available_methods
else:
    print('No Gurobi License.')

class Solver:
    def __init__(self, env=env, solver_name='MdpSolver', solve_method='vi'):
        self.env = env
        self.solver_name = solver_name
        self.solve_method = solve_method
        self.available_solvers = available_solvers
        
        if self.solver_name == 'MdpSolver':
            self.solver = MdpSolver(self.env, self.solve_method)
        elif self.solver_name == 'MarmoteSolver':
            self.solver = MarmoteSolver(self.env, self.solve_method)
        elif self.solver_name == 'GurobiSolver':
            self.solver = GurobiSolver(self.env, self.solve_method)

    def build(self):
        self.solver.build()

    def run(self):
        self.solver.run()
        # self.value = self.solver.value
        # self.policy = self.solver.policy