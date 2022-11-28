from util import gurobi_license

solve_methods = []

from solvers.mdptoolbox_method import mtb_vi as mdptoolbox_value_iteration
from solvers.mdptoolbox_method import mtb_vigs as mdptoolbox_value_iteration_GS
from solvers.mdptoolbox_method import mtb_pi as mdptoolbox_policy_iteration
from solvers.mdptoolbox_method import mtb_pim as mdptoolbox_policy_iteration_modified

solve_methods = solve_methods + ['mdptoolbox_value_iteration',
                                 'mdptoolbox_value_iteration_GS',
                                 'mdptoolbox_policy_iteration',
                                 'mdptoolbox_policy_iteration_modified']

try:
    from solvers.marmote import m_vi as marmote_value_iteration
    from solvers.marmote import m_vigs as marmote_value_iteration_GS
    from solvers.marmote import m_pi as marmote_policy_iteration
    from solvers.marmote import m_pim as marmote_policy_iteration_modified
    solve_methods = solve_methods + ['marmote_value_iteration', 
                                     'marmote_value_iteration_GS',
                                     'marmote_policy_iteration',
                                     'marmote_policy_iteration_modified',]
except:
    print('Marmote is not working currently.')

if gurobi_license():
    from solvers.gurobi import g_pl as gurobi_pl
    from solvers.gurobi import g_pl_dual as gurobi_pl_dual
    solve_methods = solve_methods + ['gurobi_pl',
                                    'gurobi_pl_dual']

def solve(env, solving_method=solve_methods[0]):
    return globals()[solving_method](env)