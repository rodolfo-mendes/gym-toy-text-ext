from gym.envs.registration import register

register(
    id="RandomFrozenLake-v0",
    entry_point="gym_toy_text_ext.envs:RandomFrozenLakeEnv"
)