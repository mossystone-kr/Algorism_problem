import time
import gymnasium as gy


env = gy.make("CartPole-v1", render_mode="rgb_array")
env.reset()
env.render()
action = env.action_space.sample()
time.sleep(10)

print(action)
