import importlib

envs_list = ['Ex10', 'Ex20', 'Ex30', 'Ex31', 'Ex40', 'frozen_lake_eight', 'frozen_lake', 'taxi', 'example']
envs_list = ['environments.'+elem for elem in envs_list]

def make_env(env_name):
    return importlib.import_module(env_name).mdp_env