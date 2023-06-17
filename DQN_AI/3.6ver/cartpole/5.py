import gym

env = gym.make('CartPole-v1')

observation = env.reset()
print("1 :", observation)

observation, reward, done, info = env.step(0)
# observation, reward, done, info = env.step(1)
print("2 :", observation)

env.close()