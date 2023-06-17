import gym

env = gym.make('CartPole-v1')

print('action_space           : ', env.action_space)
print('observation_space      : ', env.observation_space)

print('observation_space.high : ', env.observation_space.high)
print('observation_space.low  : ', env.observation_space.low)