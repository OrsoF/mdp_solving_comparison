from environments.Ex10 import MdpEnv as Ex10
from environments.Ex20 import MdpEnv as Ex20
from environments.Ex30 import MdpEnv as Ex30
from environments.Ex31 import MdpEnv as Ex31
from environments.Ex40 import MdpEnv as Ex40
from environments.frozen_lake import MdpEnv as froz_l
from environments.frozen_lake_eight import MdpEnv as froz_l_e
from environments.taxi import MdpEnv as taxi
from environments.four_rooms_grid import Rooms as rooms


# envs_list = ['Ex10',
#              'Ex20', 
#              'Ex30',
#              'Ex31',
#              'Ex40',
#              'froz_l_e',
#              'froz_l',
#              'taxi']
envs_list = []
for i in range(1, 20, 1):
    envs_list.append('rooms'+'_'+str(i))


def make_env(env_name=envs_list[0]):
    if 'rooms' not in env_name:
        return globals()[env_name]()
    else:
        n = int(env_name.split('_')[1])
        env_name = 'rooms'
        return globals()[env_name](n)

