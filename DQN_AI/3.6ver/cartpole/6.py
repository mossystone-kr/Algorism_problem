import gym

env = gym.make('CartPole-v1')

max_time_step = 10
action        = 0
# action        = 1

env.reset()

for time_step in range(max_time_step):

    env.render()

    observation, reward, done, info = env.step(action)

    print(observation, done)

    if done:
        print("Max Time Step : ", time_step + 1)
        break

env.close()