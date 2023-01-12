import platform
import os
from time import time
import pandas as pd
from mdptoolbox.mdp import ValueIteration
from datetime import timedelta
import matplotlib.pyplot as plt
import numpy as np

from util import MdpGym, gurobi_license, check_environment

###### Environments ######

from environments.Ex10 import Mdp as Ex10
from environments.Ex20 import Mdp as Ex20
from environments.Ex30 import Mdp as Ex30
from environments.Ex31 import Mdp as Ex31
from environments.Ex40 import Mdp as Ex40
from environments.rooms import Mdp as Rooms

Ex10, Ex20, Ex30, Ex31, Ex40 = Ex10(), Ex20(), Ex30(), Ex31(), Ex40()

available_envs = []
available_envs = [Ex10, Ex20, Ex30, Ex31, Ex40]
# available_envs.append(MdpGym("Taxi-v3"))
available_envs.append(MdpGym("FrozenLake8x8-v1"))
available_envs.append(MdpGym("FrozenLake-v1"))
room_size_range = 2, 6
for n in range(*room_size_range):
    available_envs.append(Rooms(n))

###### Solvers ######

available_solvers = []
if gurobi_license():
    from solvers.gurobi import GurobiSolverPL, GurobiSolverPLDual
    available_solvers = [GurobiSolverPL, GurobiSolverPLDual]

if platform.system() == 'Linux':
    from solvers.marmote import MarmoteSolverVI, MarmoteSolverVIGS, MarmoteSolverPI, MarmoteSolverPIM
    available_solvers.extend([MarmoteSolverVI, MarmoteSolverVIGS, MarmoteSolverPI, MarmoteSolverPIM])

from solvers.mdptoolbox_method import MdpTBSolverVI, MdpTBSolverVIGS, MdpTBSolverPI, MdpTBSolverPIM
available_solvers.extend([MdpTBSolverVI, MdpTBSolverVIGS, MdpTBSolverPI, MdpTBSolverPIM])

###### Experience ######

class Experience:
    def __init__(self,
                 n_exp=2,
                 environments=available_envs,
                 solvers=available_solvers):
        self.n_exp = n_exp
        self.environments = environments
        self.solvers = solvers
        for env in self.environments:
            check_environment(env)

    def get_true_solutions(self, env):
        pi_mdptoolbox = ValueIteration(env.P, env.R, env.gamma, epsilon=10e-2)
        pi_mdptoolbox.run()
        return np.array(pi_mdptoolbox.V), np.array(pi_mdptoolbox.policy)

    def run_experience(self):
        if 'runtimes.csv' in os.listdir(os.getcwd()):
            print('Already done.')
        else:
            t = time()
            columns = {sol.__name__ : 0 for sol in self.solvers}

            self.runtimes = pd.DataFrame(columns, index=[env.__name__ for env in self.environments])

            for env in self.environments:
                self.true_V, self.true_policy = self.get_true_solutions(env)

                for solver in self.solvers:
                    print(env, solver)
                    for _ in range(self.n_exp):
                        solver_env = solver(env)
                        solver_env.build()
                        solver_env.run()
                        total_time = solver_env.total_time
                        self.runtimes.loc[env.__name__, solver_env.__name__] += total_time

            func = lambda x : x/self.n_exp*10**(-9)
            self.runtimes = self.runtimes.transpose().apply(func)

            self.runtimes.to_csv('runtimes.csv')

            print()

            print(self.runtimes)

            print()
            print(timedelta(seconds=time()-t))


    def reset(self):
        if 'runtimes.csv' in os.listdir(os.getcwd()):
            os.remove(os.path.join(os.getcwd(), 'runtimes.csv'))
            print('Reset successful.')
        else:
            print('No experience to reset.')

    def show(self):
        print('Total run times')
        print()
        print(self.runtimes)

    def show_latex(self):
        print(self.runtimes.style.to_latex())

    def plot_results(self):
        df = pd.read_csv('runtimes.csv', index_col=False)
        df = df.transpose()
        mapper = {i : list(df.iloc[0])[i] for i in range(len(df.columns))}
        df = df.rename(columns = mapper)
        df = df.drop('Unnamed: 0')
        df.plot(logy=True)
        plt.show()

exp = Experience()
exp.reset()
exp.run_experience()
exp.plot_results()