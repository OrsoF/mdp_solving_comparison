class Solver:
    def __init__(self, env, solver) -> None:
        self.env = env
        self.solver = solver

    def build(self):
        self.solver = self.solver(self.env.P, self.env.R, self.env.gamma, self.env.epsi)

    def run(self):
        self.solver.run()
        self.value = self.solver.value
        self.policy = self.solver.policy

from util import gurobi_license

solve_methods = []

from solvers.mdptoolbox_method import mtb_vi as mdpTB_VI
from solvers.mdptoolbox_method import mtb_vigs as mdpTB_VIGS
from solvers.mdptoolbox_method import mtb_pi as mdpTB_PI
from solvers.mdptoolbox_method import mtb_pim as mdpTB_PIM

solve_methods = solve_methods + ['mdpTB_VI',
                                 'mdpTB_VIGS',
                                 'mdpTB_PI',
                                 'mdpTB_PIM']

try:
    from solvers.marmote import m_vi as marmoteVI
    from solvers.marmote import m_vigs as marmoteVIGS
    from solvers.marmote import m_pi as marmotePI
    from solvers.marmote import m_pim as marmotePIM
    solve_methods = solve_methods + ['marmoteVI', 
                                     'marmoteVIGS',
                                     'marmotePI',
                                     'marmotePIM']
except:
    print('Marmote is not working currently.')

from solvers.gurobi import g_pl as gurobi_pl
from solvers.gurobi import g_pl_dual as gurobi_pl_dual

if gurobi_license():
    from solvers.gurobi import g_pl as gurobi_pl
    from solvers.gurobi import g_pl_dual as gurobi_pl_dual
    solve_methods = solve_methods + ['gurobi_pl',
                                    'gurobi_pl_dual']
else:
    print('No Gurobi License.')

def solve(env, solving_method=solve_methods[0]):
    return globals()[solving_method](env)