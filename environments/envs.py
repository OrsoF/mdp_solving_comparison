from environments.Ex10 import MdpEnv as Ex10
from environments.Ex20 import MdpEnv as Ex20
from environments.Ex30 import MdpEnv as Ex30
from environments.Ex31 import MdpEnv as Ex31
from environments.Ex40 import MdpEnv as Ex40
from environments.frozen_lake import MdpEnv as frozen_lake
from environments.frozen_lake_eight import MdpEnv as frozen_lake_eight
from environments.taxi import MdpEnv as taxi

envs_list = ['Ex10',
             'Ex20', 
             'Ex30',
             'Ex31',
             'Ex40',
             'frozen_lake_eight',
             'frozen_lake',
             'taxi']

def make_env(env_name=envs_list[0]):
    return globals()[env_name]()

