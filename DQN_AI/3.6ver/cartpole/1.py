import gym

env = gym.make('CartPole-v1')

env.reset()
action = env.action_space.sample()

print(action)