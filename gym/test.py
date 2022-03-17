import gym

env = gym.make('CartPole-v1') # 定义使用 gym 库中的那一个环境
# env = gym.make('CartPole-v0') # 定义使用 gym 库中的那一个环境
# env = env.umwrapped # 不做这个会有很多限制

print(env.action_space) # 查看这个环境中可用的 action 有多少个
print(env.observation_space) # 查看这个环境可用的 state 的 observation

print(env.observation_space.high) # 查看 observation 最高取值
print(env.observation_space.low) # 查看 observation 最低取值



from gym import spaces
space = spaces.Discrete(8)
x = space.sample()
print(space)
print(x)
print(space.n)

assert space.contains(x)
assert space.n == 8
