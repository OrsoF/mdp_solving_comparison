import pandas as pd
# from environments.envs import make_env, envs_list
from solvers.solvers import solve, solve_methods
import os
from tqdm import tqdm
from time import time
from datetime import timedelta
from util import check_environment
from mdptoolbox.mdp import PolicyIteration
from envs import MdpEnv

class Experience:
    def __init__(self, 
                 n_exp=1, 
                 env_maker=MdpEnv,
                 solve=solve,
                 solve_methods=solve_methods, 
                 output_path=''):
        self.n_exp = n_exp
        self.env_maker = env_maker()
        self.envs_list = self.env_maker.available_envs[:3]
        self.solve = solve
        self.solve_methods = solve_methods
        self.output_path = output_path

    def run_experience(self):
        if 'runtimes.csv' in os.listdir(os.path.join(os.getcwd(), self.output_path)):
            self.runtimes
            print('Already done.')
        else:
            t = time()
            columns = {solver : [0.]*len(self.envs_list) for solver in self.solve_methods}
            runtimes = pd.DataFrame(columns, index=self.envs_list)

            for solver in self.solve_methods:
                for env_name in self.envs_list:
                    print(solver, env_name)
                    self.env_maker.make_env(env_name)
                    env = self.env_maker

                    check_environment(env)

                    pi_mdptoolbox = PolicyIteration(env.P, env.R, env.gamma, max_iter=10e5)
                    pi_mdptoolbox.run()
                    self.true_V = pi_mdptoolbox.V
                    self.true_policy = pi_mdptoolbox.policy

                    for _ in range(self.n_exp):
                        runtime = self.solve(env, solver)
                        runtimes.loc[env_name, solver] += runtime

            func = lambda x : 10**(-9)*x/self.n_exp
            self.runtimes = pd.DataFrame(runtimes).transpose().apply(func)

            self.runtimes.to_csv('runtimes.csv')

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
exp.show()