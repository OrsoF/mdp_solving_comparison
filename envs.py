import numpy as np
from mdptoolbox.util import check
import gym
from util import MdpGym

from environments.Ex10 import Mdp as mdp_ex10
from environments.Ex20 import Mdp as mdp_ex20
from environments.Ex30 import Mdp as mdp_ex30
from environments.Ex31 import Mdp as mdp_ex31
from environments.Ex40 import Mdp as mdp_ex40
from environments.rooms import Mdp as mdp_rooms



class MdpEnv:
    def __init__(self):
        self.available_envs = ['Ex10',
                              'Ex20',
                              'Ex30',
                              'Ex31',
                              'Ex40',
                              'four_rooms',
                              'frozen_lake_eight',
                              'frozen_lake',
                              'taxi']
        self.gamma = 0.999
        self.epsi = 1e-5

    def make_env(self, env_name, dim=5):
        assert env_name in self.available_envs

        self.dim = dim
        if env_name == 'taxi':
            self.env = MdpGym("Taxi-v3")
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'frozen_lake':
            self.env = MdpGym("Taxi-v3")
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'frozen_lake_eight':
            self.env = MdpGym("FrozenLake8x8-v1")
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'Ex10':
            self.env = mdp_ex10()
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'Ex20':
            self.env = mdp_ex20()
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'Ex30':
            self.env = mdp_ex30()
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'Ex31':
            self.env = mdp_ex31()
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'Ex40':
            self.env = mdp_ex40()
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
        elif env_name == 'four_rooms':
            self.env = mdp_rooms(self.dim)
            self.P, self.R = self.env.P, self.env.R
            self.S, self.A = self.env.S, self.env.A
