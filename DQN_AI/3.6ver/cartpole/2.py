import gym
# import random

env = gym.make('CartPole-v1')

observation = env.reset()
action = env.action_space.sample()
# action = random.randrange(0, 2)
step = env.step(action)

print('observation : ', observation)
print('action      : ', action)
print('step        : ', step)