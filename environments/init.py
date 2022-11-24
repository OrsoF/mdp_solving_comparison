import importlib
import os

envs_list = os.listdir(os.path.join(os.getcwd(), 'environments'))
try:
    envs_list.remove('__pycache__')
    envs_list.remove('init.py')
except:
    pass

def make_env(env_name):
    return importlib.import_module(env_name).MdpEnv
