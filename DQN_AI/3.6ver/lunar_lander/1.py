import gym
import time


env = gym.make("LunarLander-v2")

episode_number  = 1
timestep_number = 100

for episode in range(episode_number):

    observation = env.reset()

    for timestep in range(timestep_number):

        env.render()

        action = 2
        observation, reward, done, info = env.step(action)

        if done:
            print('episode : ', episode + 1, ' Max Timestep :', timestep + 1)
            break

env.close()