import importlib
import os

envs_list = list(filter(lambda elem : elem[0] != '_', 
                 os.listdir(os.path.join(os.getcwd(), 'environments'))))
envs_list = ['environments.'+elem[:-3] for elem in envs_list]

def make_env(env_name):
    return importlib.import_module(env_name).MdpEnv