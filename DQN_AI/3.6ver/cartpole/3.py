import gym
# import random

env = gym.make('CartPole-v1')

episode_number  = 3
timestep_number = 100

for episode in range(episode_number):

  observation = env.reset()

  for timestep in range(timestep_number):

      env.render()

      print(observation)

      action = env.action_space.sample()
      # action = random.randrange(0, 2)
      observation, reward, done, info = env.step(action)

      if done:

          print('episode : ', episode + 1, ' Max Timestep :', timestep + 1)
          break

env.close()