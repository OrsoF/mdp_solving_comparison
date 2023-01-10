import pandas as pd
# from environments.envs import make_env, envs_list
from solvs import Solver
import os
from tqdm import tqdm
from time import time
from datetime import timedelta
from util import check_environment
from mdptoolbox.mdp import ValueIteration
from envs import MdpEnv

class Experience:
    def __init__(self, 
                 n_exp=2, 
                 env_maker=MdpEnv,
                 solver=Solver,
                 output_path=''):
        self.n_exp = n_exp
        self.env_maker = env_maker()
        self.envs_list = self.env_maker.available_envs
        self.sol = solver
        self.solver_name = list(self.sol().available_solvers.keys())
        self.output_path = output_path

    def run_experience(self):
        if 'runtimes.csv' in os.listdir(os.path.join(os.getcwd(), self.output_path)):
            print('Already done.')
        else:
            t = time()
            columns = {sol_instance+'_'+sol_method : 0. for sol_instance in self.sol().available_solvers 
                                                   for sol_method in self.sol().available_solvers[sol_instance]}
            self.runtimes = pd.DataFrame(columns, index=self.envs_list)

            print()

            for env_name in self.envs_list:
                self.env_maker.make_env(env_name)
                env = self.env_maker

                check_environment(env)

                pi_mdptoolbox = ValueIteration(env.P, env.R, env.gamma, epsilon=10e-2)
                # pi_mdptoolbox.verbose = True
                pi_mdptoolbox.run()
                self.true_V = pi_mdptoolbox.V
                self.true_policy = pi_mdptoolbox.policy

                for sol_instance in self.sol().available_solvers:
                    for sol_method in self.sol().available_solvers[sol_instance]:
                        print()
                        print(sol_instance, sol_method, env_name)

                        for _ in range(self.n_exp):
                            local_sol = self.sol(env, sol_instance, sol_method)
                            local_sol.build()
                            local_sol.run()

                            total_time = local_sol.solver.total_time
                            
                            sol_name = sol_instance + '_' + sol_method

                            self.runtimes.loc[env_name, sol_name] += total_time

            func = lambda x : x/self.n_exp*10**(-9)
            self.runtimes = self.runtimes.transpose().apply(func)

            self.runtimes.to_csv('runtimes.csv')

            print()

            print(self.runtimes)

            print()
            print(timedelta(seconds=time()-t))


    def reset(self):
        if 'runtimes.csv' in os.listdir(os.path.join(os.getcwd(), self.output_path)):
            os.remove(os.path.join(os.getcwd(), self.output_path, 'runtimes.csv'))
            print('Reset successful.')
        else:
            print('No experience to reset.')

    def show(self):
        print('Total run times')
        print()
        print(self.runtimes)

    def show_latex(self):
        print(self.runtimes.style.to_latex())

exp = Experience()
exp.reset()
exp.run_experience()
# exp.show()
