import gym
import random

env = gym.make('CartPole-v1')

max_time_step = 2000

max_episode = 100

observation = env.reset()

for time_step in range(max_time_step):

    env.render()

    if observation[2] >= 0.1:
        for i in range(2):
            action = 1
    elif observation[2] <= -0.1:
        for i in range(2):
            action = 0
    elif observation[2] > 0:
        if observation[3] > 0:
            action = 1
        else:
            action = 0
    elif observation[2] < 0:
        if observation[3] < 0:
            action = 0
        else:
            action = 1
    else:
        action = random.randrange(0, 2)

    observation, reward, done, info = env.step(action)

    if observation[0] > 0.7:
        if observation[2] > 0:
            for i in range(2):
                action = 1
                observation, reward, done, info = env.step(action)
    elif observation[0] < -0.7:
        if observation[2] < 0:
            for i in range(2):
                action = 0
                observation, reward, done, info = env.step(action)

    print(observation, reward, done)

    if done:
        print("Max Time Step :", time_step + 1)
        break

env.close()