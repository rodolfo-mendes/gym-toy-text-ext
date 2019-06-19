from gym.envs.toy_text.frozen_lake import generate_random_map
from gym.envs.toy_text.frozen_lake import FrozenLakeEnv

class RandomFrozenLakeEnv(FrozenLakeEnv):
    def __init__(self, size=8, p=0.8, is_slippery=True):
        desc = generate_random_map(size, p)
        super(RandomFrozenLakeEnv, self).__init__(desc=desc, is_slippery=is_slippery)
